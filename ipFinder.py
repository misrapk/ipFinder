import socket
import time


dnsName = "cognizant.com" #enter server name
while True:
    ip = socket.gethostbyname(dnsName)
    print(ip)
    time.sleep(900)   #15 minutes(15*60 = 900s)