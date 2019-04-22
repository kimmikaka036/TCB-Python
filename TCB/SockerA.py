import asyncore
import socket 

 
class Server(asyncore.dispatcher):
    def __init__(self, address):
        asyncore.dispatcher.__init__(self) 
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(5)

    def handle_accept(self):
        # Called when a client connects to our socket
        client_info = self.accept()
        if client_info is not None:
            ClientHandler(client_info[0], client_info[1])
    

class ClientHandler(asyncore.dispatcher):
    def __init__(self, sock, address):
        asyncore.dispatcher.__init__(self, sock)
        self.data_to_write = []

    def writable(self):
        return bool(self.data_to_write)

    def handle_write(self):
        data = self.data_to_write.pop()
        sent = self.send(data[:1024]) 
        print('handle_write')
        if sent < len(data): 
            print('sent < len(data)')
            remaining = data[sent:]
            self.data_to_write.append(remaining) 

    def handle_read(self):
        data = self.recv(1024)
        if(len(data) > 0):  
            print('handle_read() -> (%d) "%s"', len(self.data_to_write), data.rstrip()) 
            self.data_to_write.insert(0, data)
    
    def handle_close(self): 
        self.close()



def main(): 
    HOST = '0.0.0.0'
    PORT = 4000
    s = Server((HOST,PORT))
    asyncore.loop()


if __name__ == '__main__':
    main() 