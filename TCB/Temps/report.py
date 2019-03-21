import base64 
import numpy as np
import cv2 
import face_recognition
import os
import re
 
from io import BytesIO 
from PIL import Image  


import xlsxwriter 
from adapterVerification import adapterVerification

class report: 
        def main():   
                #  C:\\Users\\srirath\\Pictures\\calfw\\aligned images
                workbook = xlsxwriter.Workbook('Expenses01.xlsx')
                worksheet = workbook.add_worksheet('Positive')
                worksheet2 = workbook.add_worksheet('Nagative')  

                worksheet.write(1, 1,   "Unknown Image")
                worksheet.write(1, 2, "Known Image") 
                worksheet.write(1,3, "Result")
 
                worksheet2.write(1, 1,   "Unknown Image")
                worksheet2.write(1, 2, "Known Image") 
                worksheet2.write(1,3, "Result")

                row = 2 
                rowNagative = 2
                # C:\\Users\\srirath\\Pictures\\calfw\\aligned images
                onlyfiles = os.listdir("C:\\Users\\srirath\\Pictures\\calfw\\aligned images")  
                limit = len(onlyfiles)  
                for i,item in enumerate(onlyfiles): 
                        if i != limit-1:
                           nexts = i
                           current =onlyfiles[i]
                           previous=onlyfiles[nexts+1]

                           with open("C:\\Users\\srirath\\Pictures\\calfw\\aligned images\\"+current, "rb") as image_file:
                                unknown_encoding = base64.b64encode(image_file.read())

                           with open("C:\\Users\\srirath\\Pictures\\calfw\\aligned images\\"+previous, "rb") as image_file:
                                known_encoding = base64.b64encode(image_file.read())
 
                           is_same_person =adapterVerification.execute(unknown_encoding,known_encoding) 
                           currentfileName = current.split("_000")
                           previousFileName= previous.split("_000")
                           print(currentfileName[0]+" | "+previousFileName[0])  
                           if currentfileName[0] == previousFileName[0]:
                                worksheet.write(row, 1,   current)
                                worksheet.write(row, 2, previous) 
                                worksheet.write(row,3, str(is_same_person))
                                row += 1
                           else:
                                worksheet2.write(rowNagative, 1,   current)
                                worksheet2.write(rowNagative, 2, previous) 
                                worksheet2.write(rowNagative,3, str(is_same_person))  
                                rowNagative +=1
                          
                            
                workbook.close()

        if __name__ == '__main__': 
                main() 