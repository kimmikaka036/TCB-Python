import SocketServer
import socket

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = socket.gethostname(), 4000

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
