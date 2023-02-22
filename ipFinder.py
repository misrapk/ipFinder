import socket
import time


dnsName = input("ENTER SERVER: ") #enter server name
ipadr = socket.gethostbyname(dnsName)

while True:
    newIp = socket.gethostbyname(dnsName)
    if(newIp != ipadr):
        ipadr = newIp
        print(f"IP CHANGED! New IP: {ipadr}")
    print(f"IP: {ipadr}")
        
    time.sleep(900)   #15 minutes(15*60 = 900s)

