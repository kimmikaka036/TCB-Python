import socket 
import asyncore 
import os
import base64
import dlib
import cv2
import openface
import numpy 
import gc
import sys


from io import BytesIO
from PIL import Image

numpy.set_printoptions(precision=2)

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
        rgbImg = cv2.cvtColor(numpy.array(pimg), cv2.COLOR_RGB2BGR)   

        bb = align.getLargestFaceBoundingBox(rgbImg)  
        alignedFace = align.align(96, rgbImg, bb,landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        del sbuf
        del pimg
        del rgbImg
        del bb  
        return alignedFace

class AdapterVerification(implements(VerifyInterface)): 
    def execute(self, known_img,unknown_img,net): 
       
        try:
            img1 = net.forward(known_img)
            img2 = net.forward(unknown_img) 
            d = img1 - img2
            del net
            del img1
            del img2 
            return "{:0.3f}".format(numpy.dot(d, d))
        except:
            return None
        
        

  

class EchoHandler(asyncore.dispatcher_with_send): 
 
   
    def handle_read(self):  
        data = self.recv(5000) 
        if data:  
            data = data.decode('utf-8')
            
            if(data[-2:] =="##"):

                sourceMail = data.split('_')
                if(len(sourceMail) > 0): 
                    fileName ="base_"+sourceMail[0]+".txt"
                    read = open(fileName, "r")
                    encodeImage = read.read() +sourceMail[1]
                    read.close() 

                    alignment = AdapterAlignment() 
                    align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')
                    
                    fileDir = os.path.dirname(os.path.realpath(__file__))
                    modelDir = os.path.join(fileDir, '..', 'models')
                    openfaceModelDir = os.path.join(modelDir, 'openface')
    
                
                    source =encodeImage.split('|')
                    encode_1 = source[0]
                    encode_2 = source[1]  
            

                    result_1= alignment.execute(encode_1,align) 
                    result_2= alignment.execute(encode_2[:-2],align) 

                    verify = AdapterVerification()
                    net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96) 
                    result = verify.execute(result_1,result_2,net)

                    if(result is not None):
                        if(float(result) < 1.00):
                                if(int(sourceMail[0]) % 45 == 0 and  int(sourceMail[0]) != 0): 
                                    result = 'true|'+result+'#'
                                else:
                                     result = 'true|'+result
                        else:
                            
                                if(int(sourceMail[0]) % 45 == 0 and  int(sourceMail[0]) != 0): 
                                    result = 'false|'+result+'#'
                                else:
                                    result = 'false|'+result 

                    else:
                                if(int(sourceMail[0]) % 45 == 0 and  int(sourceMail[0]) != 0): 
                                    result = 'None#' 
                                else:
                                    result = 'None' 

                        
                    print("RESULT : "+result) 
                    os.remove(fileName)
                gc.collect()
                
                self.send(result.encode()) 

                print(int(sourceMail[0]))
                if(int(sourceMail[0]) % 45 == 0 and  int(sourceMail[0]) != 0): 
                    print("Terminate")  
                    exit()

                 
            else: 
                sourceMail = data.split('_')
                if(len(sourceMail) > 0): 
                    f = open("base_"+sourceMail[0]+".txt", "a")
                    f.write(sourceMail[1])
                    f.close()  
                result ='xxx'
                self.send(result.encode())  
             
     
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