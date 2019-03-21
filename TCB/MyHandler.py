import socket
 

HOST = ''                # Symbolic name meaning all available interfaces
PORT = 4000              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100) 
conn, addr = s.accept()
while True: 
        print('Connected by', addr)
        data = conn.recv(10024) 
        if not data:
            break
        data = data.decode('utf-8')
        conn.send(data.encode()) 
conn.close()