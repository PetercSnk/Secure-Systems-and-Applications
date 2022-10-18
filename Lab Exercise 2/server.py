# server.py 
import socket 
import time 
import Caesarcipher1func as c1
import Caesarcipher2func as c2

# create a socket object 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name 
#host = '127.0.0.1'
host = socket.gethostname()

port = 9999

# bind to the port 
serversocket.bind((host, port)) 

# queue up to 5 requests 
serversocket.listen(5) 

while True:
    # establish a connection 
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr)) 

    tm = clientsocket.recv(1024)
    print(tm)
    print()
    c2.caesar2(tm.decode('utf-8'))
    
clientsocket.close()
