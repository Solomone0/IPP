import os
os.system("clear")
import socket
print("""____   _______   _____   _______     -------
  / __ \ |__   __| /   _ \ |__   __|  -====------
 | (__) |   | |    \  \ \_\   | |    -======------
 |  __  |   | |    /   \ __   | |    --====-------
 | |  | |   | |   |  (\ / /   | |     -----------
 |_|  |_|   |_|    \_____/    |_|       -------""")
print("  ")
print("  ")
a="Enter the number one or two number"
print(a.center(60))
print("  ")
print("1= Know IP \n2= Know the IP reference")
print(" ")
print(" ")
a=int(input("Enter the number one or twe : "))
while True:
		if a==1:
			m=input("Enter Your name >! ")
			if m=='done':
				break
			ip=socket.gethostbyname(m)
			print(ip)
		elif a==2:
			p=input("Enter the ip >! : ")
			if p=='done':
				break
			host=socket.gethostbyaddr(str(p))
			print(host)
		
