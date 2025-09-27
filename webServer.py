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
      
      #This variable can store the headers you want to send for any valid or invalid request. 
      #What header should be sent for a response that is ok?    
      #Fill in start 
      header = b"HTTP/1.1 200 OK\r\n"
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      #Complete header must end with \r\n\r\n
      header += outputdata + b"\r\n"
      #Fill in end
               
      body = b""
      for i in f: #for line in file
        body += i  # Fill in start - append file contents # Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command
      # Fill in start
      connectionSocket.send(header + body)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      errorHeader = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
      errorBody = b"<html><head></head><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(errorHeader + errorBody)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # DO NOT UNCOMMENT THESE WHEN SUBMITTING
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
