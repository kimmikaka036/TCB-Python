import socket 
import zlib   
import base64
import ctypes
from adapterDetect import adapterDetect
from adapterAlignment import adapterAlignment
from adapterVerification import adapterVerification

class moduleBCommand: 

    def main():  
      # unknown_encoding = data = open("test.txt", "r").read() 
      #jpg_as_text  =adapterDetect.execute('','') 
      #adapterAlignment.execute(jpg_as_text,jpg_as_text) 
      # is_same_person  = adapterVerification.execute(jpg_as_text,unknown_encoding) 
 


        HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
        PORT = 50007              # Arbitrary non-privileged port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(100) 
            conn, addr = s.accept()
            with conn: 
                while True: 
                    print('Connected by', addr)
                    data = conn.recv(10024) 
                    if not data:
                        break
                    data = data.decode('utf-8') 
                    sorce = data.split(' ') 

                    unknow_face  = adapterDetect.execute('','') 
                    unknow_face  = adapterAlignment.execute(unknow_face,'') 
                    is_same_person  = adapterVerification.execute(unknow_face,sorce[1])  
                    same_person = str(is_same_person)
                    face = unknow_face.decode()
                    dataReturn = same_person+'#'+face
                    conn.send(dataReturn.encode()) 
                conn.close()
        



    if __name__ == '__main__': 
        main() 