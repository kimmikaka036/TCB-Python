import time
import socket 
import cv2
import openface
import itertools
import argparse
import dlib
import os
import base64
import asyncore 
import gc

import numpy as np 
from io import BytesIO
from PIL import Image



np.set_printoptions(precision=2)

from interface import implements, Interface
 
class AlignmentInterface(Interface): 
    def execute(self, base64Img,align):
        pass 

class VerifyInterface(Interface): 
    def execute(self, known_img,unknown_img,net):
        pass 

class AdapterAlignment(implements(AlignmentInterface)):
    def execute(self, base64Img,align): 
      
        sbuf = BytesIO()
        sbuf.write(base64.b64decode(base64Img))
        pimg = Image.open(sbuf) 
        rgbImg = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)  
 
        # bgrImg = cv2.imread(base64Img) 
        # rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

        bb = align.getLargestFaceBoundingBox(rgbImg)  
        alignedFace = align.align(96, rgbImg, bb,landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        return alignedFace

    def isBase64(sb):
        try:
                if type(sb) == str:
                        # If there's any unicode here, an exception will be thrown and the function will return false
                        sb_bytes = bytes(sb, 'ascii')
                elif type(sb) == bytes:
                        sb_bytes = sb
                else:
                        raise ValueError("Argument must be string or bytes")
                return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
        except Exception:
                return False


class AdapterVerification(implements(VerifyInterface)): 
    def execute(self, known_img,unknown_img,net): 
       
        img1 = net.forward(known_img)
        img2 = net.forward(unknown_img)

        d = img1 - img2
        return "{:0.3f}".format(np.dot(d, d))
 

# class ModuleBCommand: 
#     def main():  
#             HOST = ''              
#             PORT = 4000       
#             LIMIT = 10000
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.bind((HOST, PORT))
#             s.listen(1) 
#             conn, addr = s.accept()  

#             verify = AdapterVerification()
#             alignment = AdapterAlignment()  

#             align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')
#             fileDir = os.path.dirname(os.path.realpath(__file__))
#             modelDir = os.path.join(fileDir, '..', 'models')
#             openfaceModelDir = os.path.join(modelDir, 'openface')

#             net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96) 


#             while True: 
#                 print('Connected by', addr) 
#                 data = conn.recv(LIMIT)  
#                 if not data:
#                     break 
#                 source =data.split('||')
#                 path_1 = source[0]
#                 path_2 = source[1] 

#                 result_1= alignment.execute(path_1,align) 
#                 result_2= alignment.execute(path_2,align) 


#                 result = verify.execute(result_1,result_2,net)

#                 if(float(result) < 1.00):
#                     result = 'true '+result
#                 else:
#                     result = 'false '+result
            
#                 print('RESULT : '+result) 
#                 conn.send(result.encode())  
#                 gc.collect() 
#             conn.close()
                
                
          

       
        


#     if __name__ == '__main__': 
#         main()    



   

class EchoHandler(asyncore.dispatcher_with_send): 
 
   
    def handle_read(self):  
        data = self.recv(5000) 
        if data:  
            data = data.decode('utf-8')   

            alignment = AdapterAlignment() 

            if(alignment.isBase64(data)):
                print("Complete base64")
            else:
                data += data

            result = 'false '
            print('RESULT : '+result) 
            self.send(result.encode())  

            # verify = AdapterVerification()
            # alignment = AdapterAlignment() 
            
            # source =data.split('||')
            
            # path_1 = source[0]
            # path_2 = source[1] 

            # align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')
 

            # result_1= alignment.execute(path_1,align) 
            # result_2= alignment.execute(path_2,align) 

            # fileDir = os.path.dirname(os.path.realpath(__file__))
            # modelDir = os.path.join(fileDir, '..', 'models')
            # openfaceModelDir = os.path.join(modelDir, 'openface')

            # net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96) 

            # result = verify.execute(result_1,result_2,net)

            # if(float(result) < 1.00):
            #     result = 'true '+result
            # else:
            #     result = 'false '+result 
             
     
    def handle_close(self):
        print('handle_close') 
        self.close()

    


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port): 
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(1)   

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair 
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)
          

server = EchoServer('', 4000)
asyncore.loop()
