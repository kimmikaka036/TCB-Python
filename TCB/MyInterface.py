import time
import socket 
import cv2
import openface
import itertools
import argparse
import dlib
import os
import base64
import numpy as np 
from io import BytesIO
from PIL import Image


np.set_printoptions(precision=2)

from interface import implements, Interface
 
class AlignmentInterface(Interface): 
    def execute(self, base64Img):
        pass 

class VerifyInterface(Interface): 
    def execute(self, known_img,unknown_img):
        pass 

class AdapterAlignment(implements(AlignmentInterface)):
    def execute(self, base64Img): 
        align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')

        sbuf = BytesIO()
        sbuf.write(base64.b64decode(base64Img))
        pimg = Image.open(sbuf) 
        rgbImg = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)  

        bb = align.getLargestFaceBoundingBox(rgbImg)  
        alignedFace = align.align(96, rgbImg, bb,landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        return alignedFace


class AdapterVerification(implements(VerifyInterface)): 
    def execute(self, known_img,unknown_img): 
        fileDir = os.path.dirname(os.path.realpath(__file__))
        modelDir = os.path.join(fileDir, '..', 'models')
        openfaceModelDir = os.path.join(modelDir, 'openface')

        net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96) 
        img1 = net.forward(known_img)
        img2 = net.forward(unknown_img)

        d = img1 - img2
        return "{:0.3f}".format(np.dot(d, d))
  
class VerificationManager: 
    def execute(self,unknown_encoding_1,unknown_encoding_2):
        alignment = AdapterAlignment() 
        result_1= alignment.execute(unknown_encoding_1) 
        result_2= alignment.execute(unknown_encoding_2) 

        verify = AdapterVerification()
        result = verify.execute(result_1,result_2)
        return result 

class ModuleBCommand: 
    def main():
        HOST = ''              
        PORT = 4000       
        LIMIT = 100000000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(100) 
        conn, addr = s.accept() 
        verify = VerificationManager() 
        while True: 
            print('Connected by', addr)
            data = conn.recv(LIMIT) 
            if not data:
                break
            data = data.decode('utf-8')
            if(data.startswith("#1#")):
                unknown_encoding_1 = data
                data ='#1#'
                conn.send(data.encode())  
                unknown_encoding_2 = None
            elif(data.startswith("#2#")):
                unknown_encoding_2 = data 
                data ='#2#'
                conn.send(data.encode()) 
            elif(data.startswith("#3#")): 
                print(unknown_encoding_1)
                print(unknown_encoding_2)
                unknown_encoding_1 = unknown_encoding_1.replace("#1#", "")
                unknown_encoding_2= unknown_encoding_2.replace("#2#", "")
                # if(not unknown_encoding_1  and not unknown_encoding_2): 
                result = verify.execute(unknown_encoding_1,unknown_encoding_2) 
                conn.send(result.encode()) 
            else:
                unknown_encoding_1 = None 
                unknown_encoding_2 = None

            
        # conn.close()
        


    if __name__ == '__main__': 
        main()    