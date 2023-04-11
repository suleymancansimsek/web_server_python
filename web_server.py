#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) # Prepare a server socket

# Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start
    
    try:
        message = connectionSocket.recv(1024).decode() # Fill in end
        filename = message.split()[1]
        f = open(filename[1:], encoding='utf-8')
        outputdata = f.read() # Fill in start
        
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) # Fill in start
        
        # Close client socket
        connectionSocket.close() # Fill in end

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
