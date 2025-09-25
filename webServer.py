# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = #Fill in start -are you accepting connections?     
    serverSocket.accept()
    #Fill in end
    
    try:
      message = #Fill in start -a client is sending you a message   
      connectionSocket.recv(1024).decode()
      #Fill in end 
      filename = message.split()[1]
      
      #opens the client requested file. 
      f = open(filename[1:],     #fill in start              
      "rb"
      #fill in end   )
      
      #This variable can store the headers you want to send for any valid or invalid request.   
      #Fill in start 
      header = b"HTTP/1.1 200 OK\r\n"
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\nServer: MyServer\r\nConnection: close\r\n\r\n"
      #Fill in end
               
      for i in f: #for line in file
      #Fill in start - append your html file contents 
        pass  # we are reading as bytes above, so loop not needed
      #Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.send(header + outputdata + f.read())
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      header = b"HTTP/1.1 404 Not Found\r\n"
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\nServer: MyServer\r\nConnection: close\r\n\r\n"
      body = b"<html><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(header + outputdata + body)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # DO NOT MOVE OR UNCOMMENT
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
