## What happens when you type a URL in the browser?

Client => Url => www.google.com
Server => Ip Address

DNS(DOMAIN NAME SERVER) => Converts domain name to IP address

Step 1 : Client sends request to DNS server
Step 2 : DNS server responds with corresponding IP address
Step 3 : Client sends request to corresponding IP address
Step 4 : Server responds with content (HTML, CSS, JS, etc.)'

Client cache the content to reduce server load frequently

Client request to Server
Server response to Client

Protocol/rules : HTTP/HTTPS (refer to the rule to understand the request and response format or in order to communicate)

PORT => Logical Number
Total Port Number : 65535
IP/Address => Physical Number
ip:port => Unique identifier for a process on a machine

1.If one machine needs to send email then the rule can be different
2.If one machine needs to send file then the rule can be different
3.If one machine needs to send HTML content then the rule can be different

http => hyper text transfer protocol
https => hyper text transfer protocol secure

Network Stack => OSI MODEL / TCP/IP MODEL
models define the steps for most of the protocols to work when one machine has to communicate withh other machine
When a client raise a request ,it needs to ho through 5 layer (TCP/IP Model)

    Application Layer
    Transport Layer
    Network Layer
    Data Link Layer
    Physical Layer

Application Layer => HTTP, HTTPS, FTP, SMTP, etc.
First layer - Application layer is responsible for end-to-end communication
Final Application layer is responsible for user interface
Logic of how the layer neds to work implemented on these apps
Protocols => Rules for communication
HTTP => Hyper Text Transfer Protocol
HTTPS => Hyper Text Transfer Protocol Secure
SMTP => Simple Mail Transfer Protocol
FTP => File Transfer Protocol
WebRTC => Web Real-Time Communication
VOIP => Voice over IP are controlled in the application layer.

Transport Layer => TCP, UDP, etc.
Second layer - Transport layer is responsible for end-to-end communication
Data collected on the application layer is passed on to the transport layer
Transport layer exists on the OS
Any Protocol You are following can be classified in one of the two categories(reliable or unreliable)
Ex of reliable : HTTP,websockets,FTP
Ex of unreliable : VoIP,NTP,UDP,DNS,TFTP
ON TRANSPAORT THERE IS TWO PROTOCOLS :
TCP => Transmission Control Protocol
UDP => User Datagram Protocol

Tcp is converted to segements before passing to network layer
Udp is converted to datagrams before passing to network layer

Network Layer => IP, ICMP, etc.
Third layer
Data collected at transport layer is passed to network layer
Logic of network layer is exist in os kernel but also in the Network drivers and hardwares
how to route tour packets
Everything in 1 protocol : IP (Internet Protocol)

Data Link Layer => Ethernet, WiFi, etc.
Fourth layer
Error detection and correction
Most of the logic of this layer is written in the NIC,OS DRIVERS ,WIFI ROUTER ,etc
(NIC - Network Interface Card)
(main networking hardware)

Physical Layer => Electrical, Optical, etc.
Actual Final Physical Wires
