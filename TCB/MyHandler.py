import socket
 

HOST = ''                # Symbolic name meaning all available interfaces
PORT = 4000              # Arbitrary non-privileged port
LIMIT = 1000000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100) 
conn, addr = s.accept()
while True: 
        print('Connected by', addr)
        data = conn.recv(LIMIT) 
        if not data:
            break
        data = data.decode('utf-8')
        imgList = data.split('###') 
        print(imgList[0])
        print(imgList[1])
        conn.send(data.encode()) 
conn.close()