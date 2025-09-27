# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)  # Fill in start: listen for connections
  # Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start - accepting connections # Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode()  # Fill in start - receive client message # Fill in end
      filename = message.split()[1]
      
      #opens the client requested file. 
      f = open(filename[1:], "rb")  # fill in start: open file in binary mode # fill in end
      
      # 200 OK headers
      header = b"HTTP/1.1 200 OK\r\n"
      header += b"Server: SimpleWebServer\r\n"
      header += b"Connection: close\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"
               
      body = b""
      for i in f: #for line in file
        body += i  # Fill in start - append file contents # Fill in end 
        
      #Send everything as one send command
      connectionSocket.send(header + body)
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # 404 Not Found headers
      errorHeader = b"HTTP/1.1 404 Not Found\r\n"
      errorHeader += b"Server: SimpleWebServer\r\n"
      errorHeader += b"Connection: close\r\n"
      errorHeader += b"Content-Type: text/html\r\n\r\n"
      errorBody = b"<html><head></head><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(errorHeader + errorBody)

      #Close client socket
      connectionSocket.close()

  # DO NOT UNCOMMENT THESE WHEN SUBMITTING
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
