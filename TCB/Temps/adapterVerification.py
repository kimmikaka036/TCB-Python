import base64 
import numpy as np
import cv2 
import face_recognition
import os
import re
 
from io import BytesIO 
from PIL import Image  



from interfaceFace import interfaceFace

class adapterVerification(interfaceFace):

        def execute(unknown_encoding,known_encoding):    
 
            known_face_encoding = adapterVerification.face_encoding(known_encoding) 
            unknown_face_encoding = adapterVerification.face_encoding(unknown_encoding) 


            # compare face
            if  unknown_face_encoding is not None and known_face_encoding is not None:
                known_faces = [known_face_encoding]
                results = face_recognition.compare_faces(known_faces, unknown_face_encoding) 
                return results
            else:
                return "None"


        def face_encoding(imageEncode):
            # convert base64 to array numpy 
            image = Image.open(BytesIO(base64.b64decode(imageEncode)))
            numpy = np.array(image)
            # encode face
            face_encoding = face_recognition.face_encodings(numpy)
            if len(face_encoding) > 0:  
                return face_encoding[0]
            else:
                return None
 