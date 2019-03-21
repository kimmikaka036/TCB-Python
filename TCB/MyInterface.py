import time
import cv2
import openface
import itertools
import argparse
import os
import numpy as np
np.set_printoptions(precision=2)

from interface import implements, Interface
 
class MyInterface(Interface):

    def method1(self, x):
        pass 
 
class MyClass(implements(MyInterface)):

    global start
    global parser
    global args 

    global align 
    global net  

    def getRep(self,imgPath):
        parser = argparse.ArgumentParser() 
        parser.add_argument('imgs', type=str, nargs='+', help="Input images.")   
        args = parser.parse_args()

        fileDir = os.path.dirname(os.path.realpath(__file__))
        modelDir = os.path.join(fileDir, '..', 'models')
        dlibModelDir = os.path.join(modelDir, 'dlib')
        openfaceModelDir = os.path.join(modelDir, 'openface')

        align = openface.AlignDlib('shape_predictor/shape_predictor_68_face_landmarks.dat')
        net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), 96)

        print("Processing {}.".format(imgPath))
        bgrImg = cv2.imread(imgPath)
        if bgrImg is None:
            raise Exception("Unable to load image: {}".format(imgPath))
        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

        print("  + Original size: {}".format(rgbImg.shape))
        
        start = time.time()
        bb = align.getLargestFaceBoundingBox(rgbImg)
        if bb is None:
            raise Exception("Unable to find a face: {}".format(imgPath))

        print("  + Face detection took {} seconds.".format(time.time() - start))
        start = time.time()
        alignedFace = align.align(96, rgbImg, bb,
                                landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(imgPath))
         
        print("  + Face alignment took {} seconds.".format(time.time() - start))

        start = time.time()
        rep = net.forward(alignedFace)
        # if args.verbose:
        #     print("  + OpenFace forward pass took {} seconds.".format(time.time() - start))
        #     print("Representation:")
        #     print(rep)
        #     print("-----\n")
        return rep

    def method1(self, x):
        
        start = time.time() 
      
        print(args.imgs)
        for (img1, img2) in itertools.combinations(args.imgs, 2):
            
            d = self.getRep(img1) - self.getRep(img2)
            print("Comparing {} with {}.".format(img1, img2))
            print("  + Squared l2 distance between representations: {:0.3f}".format(np.dot(d, d)))
 
        return x * 2
      
       
 

if __name__ == "__main__":
    objName = MyClass()
    objName.method1(1)