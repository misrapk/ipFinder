import socket
import time
from plyer import notification  

dnsName = input("ENTER SERVER: ") #enter server name
ipadr = socket.gethostbyname(dnsName)       #save the default ip address

while True:
    newIp = socket.gethostbyname(dnsName) #check for new ip everytime
    if(newIp != ipadr):
        ipadr = newIp
        print(f"IP CHANGED! New IP: {ipadr}")
        
        #give the desktop notification
        notification.notify(
            title='IP Address Changed',
            message=f'New IP: {ipadr}',
            timeout=10
        )
    else:
        print(f"IP: {ipadr}")
        
    time.sleep(900)   #15 minutes(15*60 = 900s)
