import os
os.system("clear")
import socket
print("="*20)
while True:
    a=input("Enter Your IP name : ")
    ip=socket.gethostbyname("Enter Your IP name = ",a)
    print(ip)
