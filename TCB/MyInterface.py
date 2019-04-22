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
 

class ModuleBCommand: 
    def main():
            HOST = ''              
            PORT = 4000       
            LIMIT = 100000
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, PORT))
            s.listen(1000) 
            conn, addr = s.accept()  

            verify = AdapterVerification()
            alignment = AdapterAlignment() 

            while True: 
                print('Connected by', addr)

                data = conn.recv(LIMIT)  
                if data:  
                        data = data.decode('utf-8')
                        source =data.split('|')
                        encode_1 = source[0]
                        encode_2 = source[1]
                        
                        verify = AdapterVerification()
                        alignment = AdapterAlignment() 

                        result_1= alignment.execute(encode_1) 
                        result_2= alignment.execute(encode_2) 
                        result = verify.execute(result_1,result_2)

                        if(float(result) < 1.00):
                            result = 'true '+result
                        else:
                            result = 'false '+result

                        conn.send(data.encode())
                        
                        del unknown_encoding_1  
                        del result 
                        del unknown_encoding_2  
                        del result_1
                        del result_2
                        del data

                # if(data.startswith("#1#")):
                #     data = data.decode('utf-8')
                #     unknown_encoding_1 = data 
                #     unknown_encoding_1 = unknown_encoding_1.replace("#1#", "") 
                #     data ='#1#'
    
                #     result_1= alignment.execute(unknown_encoding_1) 

                #     conn.send(data.encode())  
                    
                #     del unknown_encoding_1  
                #     del data

                # elif(data.startswith("#2#")):
                #     data = data.decode('utf-8')
                #     unknown_encoding_2 = data 
                #     unknown_encoding_2= unknown_encoding_2.replace("#2#", "")  
                    
                #     result_2= alignment.execute(unknown_encoding_2) 
                #     result = verify.execute(result_1,result_2)
                    
                #     if(float(result) < 1.00):
                #         result = 'true '+result
                #     else:
                #         result = 'false '+result
    
                #     conn.send(result.encode())  

                #     del result 
                #     del unknown_encoding_2  
                #     del result_2
                #     del data
                
                
          

       
        


    if __name__ == '__main__': 
        main()    



   

# class EchoHandler(asyncore.dispatcher_with_send): 

  
     
#     def handle_read(self): 
#         data = self.recv(60000) 
#         if data:  
#             data = data.decode('utf-8')
#             source =data.split('|')
#             encode_1 = source[0]
#             encode_2 = source[1]
            
#             verify = AdapterVerification()
#             alignment = AdapterAlignment() 

#             result_1= alignment.execute(encode_1) 
#             result_2= alignment.execute(encode_2) 
#             result = verify.execute(result_1,result_2)

#             if(float(result) < 1.00):
#                 result = 'true '+result
#             else:
#                 result = 'false '+result
    
#             #self.send(data)

#             self.send(result.encode())  

#     def handle_close(self):
#         print('handle_close') 
#         self.close()


# class EchoServer(asyncore.dispatcher):

#     def __init__(self, host, port): 
#         asyncore.dispatcher.__init__(self)
#         self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.set_reuse_addr()
#         self.bind((host, port))
#         self.listen(1)   

#     def handle_accept(self):
#         pair = self.accept()
#         if pair is not None:
#             sock, addr = pair 
#             print 'Incoming connection from %s' % repr(addr)
#             handler = EchoHandler(sock)
          

# server = EchoServer('', 4000)
# asyncore.loop()
