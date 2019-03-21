# import base64
# import numpy as np
# import cv2
# import sys 
# import dlib 

# from imageio import imread 
# from PIL import Image  
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2 
import base64
import numpy as np
import datetime
from io import BytesIO
from PIL import Image
from interfaceFace import interfaceFace


class adapterAlignment(interfaceFace):
     

    def execute(unknown_encoding,known_encoding): 
        print('========') 
        detector = dlib.get_frontal_face_detector()
        predictor  = dlib.shape_predictor('shape_predictor/shape_predictor_68_face_landmarks.dat')

        fa = FaceAligner(predictor, desiredFaceWidth=256)

        sbuf = BytesIO()
        sbuf.write(base64.b64decode(unknown_encoding))
        pimg = Image.open(sbuf) 
        image = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

        # cv2.imshow("Input", image)

        image = imutils.resize(image, width=300)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
        rects = detector(gray, 2)


        # loop over the face detections
        for rect in rects:
            # extract the ROI of the *original* face, then align the face
            # using facial landmarks
            (x, y, w, h) = rect_to_bb(rect)
            faceOrig = imutils.resize(image[y:y + h, x:x + w], width=300)
            faceAligned = fa.align(image, gray, rect)
 
 
            rec , buffer = cv2.imencode('.png', faceAligned)

            jpg_as_text = base64.b64encode(buffer)
            return jpg_as_text  
        
        # detector = dlib.get_frontal_face_detector()
        # sp  = dlib.shape_predictor('shape_predictor/shape_predictor_68_face_landmarks.dat')

 
        # img = base64.b64decode(unknown_encoding);
        # npimg = np.frombuffer(img, dtype=np.uint8)
        # img = cv2.imdecode(npimg, cv2.COLOR_BGR2GRAY)
        
        
        # dets = detector(img, 1) 
        # faces = dlib.full_object_detections()
        # for detection in dets:
        #     faces.append(sp(img, detection))

        # window = dlib.image_window()
 
        # #images = dlib.get_face_chips(img, faces, size=160, padding=0.25)
        # images = dlib.get_face_chips(img, faces, size=320)
        # for image in images:
        #     window.set_image(image)
            

        # image = dlib.get_face_chip(img, faces[0]) 
        # rec , buffer = cv2.imencode('.jpg', image)
        # jpg_as_text = base64.b64encode(buffer)   
        # return jpg_as_text    
   
    
