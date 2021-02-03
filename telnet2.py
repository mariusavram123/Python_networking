import getpass
import telnetlib

HOST = "192.168.0.205"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf term\n")
tn.write(b"interface e0/1\n")
tn.write(b"ip address 192.168.100.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))