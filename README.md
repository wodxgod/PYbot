<h1 align="center">PYbot Botnet</h1>

<p align="center">
    <img width="629" height="370" src="https://raw.githubusercontent.com/WodxTV/PYbot/master/preview.png">
</p>

**PYbot** is a basic open source [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack) [botnet](https://en.wikipedia.org/wiki/Botnet) system written in Python 3, consists of a connect and control server and a bot malware script. The system works the same way as a Qbot botnet.

# C&C Commands
Command | Description
--------|------------
help, ? | Shows list of commands
methods | Shows list of attack methods
clear, cls | Clears the console window screen
exit, logout | Disconnects from the C&C server
.vse \<host> \<duration> | Starts a VSE flood attack
.udp \<host> \<duration> \<size> | Starts a UDP flood attack
.syn \<host> \<duration> | Starts a TCP SYN flood attack
.http \<host> \<duration> | Starts a HTTP GET request flood attack

# Layer 4 Attack Vectors
- **[UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) Flood**
    - Floods target with trashed UDP packets with given size of bytes to random destination ports in range 1-65535.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/UDP_flood_attack).
- **[TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) SYN Flood**
    - Floods target with SYN TCP packets to random destination ports in range 1-65535.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/SYN_flood).
- **[VSE](https://en.wikipedia.org/wiki/Source_(game_engine)) Flood**
    - Floods target with [VSE query requests](https://developer.valvesoftware.com/wiki/Server_queries) to destination port 27015 (Source Engine port).
    - Designed to take down Source based game servers by sending legitimate traffic to the target server.

# Layer 7 Attack Vectors
- **[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) GET Request Flood**
    - Floods target with HTTP GET requests.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/HTTP_Flood).

# Installation
1. Install Git and Python 3 on your server.
2. Clone the PYbot Github repository to your server via Git.
3. Change the host address and C&C port in the configuration section in [bot.py](/bot.py) to your server address and C&C port.
4. Start the CnC server by executing the command: `$ python cnc.py <cnc port>`.
5. Add accounts in [logins.txt](/logins.txt) by using the format: `username:password`.
6. Connect to the server using [PuTTY](https://www.putty.org/) via raw socket connection.

*Compiling the malware and installing it on vulnerable devices won't be told, as it's highly illegal to do. Use of this project for illegal activities is at own risk! I'm not responsible for any of your taken actions!*

# Author
- **WodX**
    - [Github](https://github.com/WodXTV)
    - [Twitter](https://twitter.com/wodxofficial)
    - [Discord](https://profiles.pw/profile/621044372951269417)
    - [PayPal.me](https://www.paypal.com/paypalme2/wodx)

# Donate
You can donate to my PayPal at https://www.paypal.com/paypalme2/wodx <3
