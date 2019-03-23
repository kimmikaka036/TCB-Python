import time
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
    global faceAligned
    def execute(self, base64Img): 
        align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')

        sbuf = BytesIO()
        sbuf.write(base64.b64decode(base64Img))
        pimg = Image.open(sbuf) 
        rgbImg = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

        # #rotate
        # detector = dlib.get_frontal_face_detector()
        # dets = detector(rgbImg, 2)
        # faces = dlib.full_object_detections()
        # for detection in dets:
        #     faces.append(align(rgbImg, detection)) 
        # images = dlib.get_face_chips(img, faces[0], size=96) 

        #scale
        rgbImg = images
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
        return "  + Squared l2 distance between representations: {:0.3f}".format(np.dot(d, d))
  
class VerificationManager: 
    def execute(self,unknown_encoding_1,unknown_encoding_2):
        alignment = AdapterAlignment() 
        result_1= alignment.execute(unknown_encoding_1) 
        #print(result_1)
        result_2= alignment.execute(unknown_encoding_2) 
        #print(result_2)

        verify = AdapterVerification()
        result = verify.execute(result_1,result_2)
        print(result)

if __name__ == "__main__":
    objName = VerificationManager()
    with open("images/s_1.jpg", "rb") as image_file:
            unknown_encoding_1 = base64.b64encode(image_file.read())
        
    with open("images/s_1.jpg", "rb") as image_file2:
            unknown_encoding_2 = base64.b64encode(image_file2.read())

    objName.execute(unknown_encoding_1,unknown_encoding_2)
 
# class MyClass(implements(AlignmentInterface)):

#     global start
#     global parser
#     global args 

#     global align 
#     global net  

#     def getRep(self,unknown_encoding,known_encoding):
     
#         fileDir = os.path.dirname(os.path.realpath(__file__))
#         modelDir = os.path.join(fileDir, '..', 'models')
#         dlibModelDir = os.path.join(modelDir, 'dlib')
#         openfaceModelDir = os.path.join(modelDir, 'openface')

#         align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')
#         net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96)

#         print("Processing {}.".format(imgPath))
#         bgrImg = cv2.imread(imgPath)
#         if bgrImg is None:
#             raise Exception("Unable to load image: {}".format(imgPath))
#         rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

#         print("  + Original size: {}".format(rgbImg.shape))
        
#         start = time.time()
#         bb = align.getLargestFaceBoundingBox(rgbImg)
#         if bb is None:
#             raise Exception("Unable to find a face: {}".format(imgPath))

#         # print("  + Face detection took {} seconds.".format(time.time() - start))
#         start = time.time()
#         alignedFace = align.align(96, rgbImg, bb,
#                                 landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
#         if alignedFace is None:
#             raise Exception("Unable to align image: {}".format(imgPath))
        
#         print("  + Alignment size: {}".format(alignedFace.shape))
#         # print("  + Face alignment took {} seconds.".format(time.time() - start))

#         start = time.time()
#         rep = net.forward(alignedFace)

#         return rep

#     def execute(self, x):
        
#         start = time.time() 
#         parser = argparse.ArgumentParser() 
#         parser.add_argument('imgs', type=str, nargs='+', help="Input images.")   
#         args = parser.parse_args()

#         print(args.imgs)
#         for (img1, img2) in itertools.combinations(args.imgs, 2): 
#             d = self.getRep(img1) - self.getRep(img2)
#             print("Comparing {} with {}.".format(img1, img2))
#             print("  + Squared l2 distance between representations: {:0.3f}".format(np.dot(d, d)))
 
#         return x * 2
    