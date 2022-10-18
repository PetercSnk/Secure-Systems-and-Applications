# client.py 
import socket 
import Caesarcipher1func as c1
# create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name 
host = socket.gethostname()
#host = '127.0.0.1'

port = 9999

# connection to hostname on the port. 
s.connect((host, port)) 

msg = input("enter message: ")
encryptedMsg = c1.caesar1(msg, 'encrypt', 12)
#key = '12'
s.send(encryptedMsg.encode('utf-8'))
#s.send(key.encode('utf-8'))


s.close() 
