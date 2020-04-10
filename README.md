<h1 align="center">PYbot Botnet</h1>

<p align="center">
    <img width="629" height="370" src="https://raw.githubusercontent.com/WodxTV/PYbot/master/preview.png">
</p>

**PYbot** is a basic open source [denial of service](https://en.wikipedia.org/wiki/Denial-of-service_attack) [botnet](https://en.wikipedia.org/wiki/Botnet) system written in Python 3, consists of a connect and control server and a bot malware script.

# C&C Commands
Command | Description
--------|------------
help, ? | Shows list of commands
methods | Shows list of attack methods
clear, cls | Clears the console window screen
exit, logout | Disconnects from the C&C server
.syn \<host> \<port> \<duration> | Starts a TCP SYN flood attack
.tcp \<host> \<port> \<duration> \<size> | Starts a TCP junk flood attack
.udp \<host> \<port> \<duration> \<size> | Starts a UDP junk flood attack
.vse \<host> \<port> \<duration> | Starts a VSE query flood attack
.http \<host> \<duration> | Starts a HTTP GET request flood attack

# Layer 4 Attack Vectors
- **[TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) Flood**
    - Floods target with trashed TCP data packets.
- **[TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) SYN Flood**
    - Floods target with SYNchronize TCP packets.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/SYN_flood).
- **[UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol) Flood**
    - Floods target with trashed UDP data packets.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/UDP_flood_attack).

# Layer 7 Attack Vectors
- **[VSE](https://en.wikipedia.org/wiki/Source_(game_engine)) Flood**
    - Floods target with [VSE server queries](https://developer.valvesoftware.com/wiki/Server_queries).
    - Designed to take down Source based game servers by sending legitimate traffic to the target server.
- **[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) GET Request Flood**
    - Floods target with HTTP GET requests.
    - Read more about the attack method [here](https://en.wikipedia.org/wiki/HTTP_Flood).

# Installation
1. Install Git and Python 3 on your server.
2. Clone the PYbot Github repository to your server via Git: `$ git clone https://github.com/WodxTV/PYbot.git`.
3. Change the host address and C&C port in the configuration section in [bot.py](/bot.py) to your server address and C&C port.
4. Start the CnC server by executing the command: `$ python cnc.py <cnc port>`.
5. Add accounts in [logins.txt](/logins.txt) using the format: `username:password`.
6. Connect to the server through [PuTTY](https://www.putty.org/) on a raw socket connection.

*Compiling the malware and installing it on vulnerable devices won't be told as it's highly illegal to get remote access to devices without permission. Use of this project for illegal activities is at own risk! I'm not responsible for any of your taken actions!*

# Author
- **wodx**
    - [Twitter](https://twitter.com/wodxgod)
    - [YouTube](https://youtube.com/wodxgod)
    - [PayPal](https://www.paypal.com/paypalme2/wodx)