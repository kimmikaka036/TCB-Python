import numpy as np
import cv2
import sys
import time
import base64 
import datetime
from interfaceFace import interfaceFace


class adapterDetect(interfaceFace):

    def execute(unknown_encoding,known_encoding):   
        face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
        video_capture = cv2.VideoCapture(0)
          
        global roi_color_orgin
        global roi_color
        global jpg_as_text
        # global jpg_as_text

        while True:
            _,img = video_capture.read() 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                roi_color_orgin = img[y:y+h, x:x+w] 
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w] 
                # eyes = eye_cascade.detectMultiScale(roi_gray) 
                # for (ex,ey,ew,eh) in eyes:
                #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


            cv2.imshow('video',img) 
            if cv2.waitKey(25) == 27:
                break 
                 
        rec , buffer = cv2.imencode('.png', img)
        cv2.imwrite("result\\original\\"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".png", roi_color_orgin )
        jpg_as_text = base64.b64encode(buffer) 
        cv2.destroyAllWindows()  
        video_capture.release()  
        return jpg_as_text
    
 
     