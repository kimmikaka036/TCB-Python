import socket 
from VerificationManager import VerificationManager

HOST = ''                # Symbolic name meaning all available interfaces
PORT = 4000              # Arbitrary non-privileged port
LIMIT = 1000000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100) 
conn, addr = s.accept()
objName = VerificationManager() 
while True: 
        print('Connected by', addr)
        data = conn.recv(LIMIT) 
        if not data:
            break
        data = data.decode('utf-8')
        imgList = data.split('###') 
        unknown_encoding_1 = imgList[0]
        unknown_encoding_2 = imgList[1]
        objName.execute(unknown_encoding_1,unknown_encoding_2) 
        conn.send(data.encode()) 
conn.close()