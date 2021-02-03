#router telnet script for loopback interfaces and ospf enabling

import getpass
import telnetlib

HOST = "192.168.20.1"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"interface loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"interface loopback 2\n")
tn.write(b"ip address 3.3.3.3 255.255.255.255\n")
tn.write(b"interface loopback 3\n")
tn.write(b"ip address 4.4.4.4 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 192.268.20.0 0.0.0.255 area 0\n")
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))