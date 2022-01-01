import socket
a=input("Enter Your IP name : ")
ip=socket.gethostbyname(a)
print(ip)
