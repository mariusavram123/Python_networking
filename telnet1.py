import getpass
import telnetlib

HOST = "192.168.0.200"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf term\n")

for n in range(10, 100, 10):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name VLAN_" + str(n).encode('ascii') + b"_python\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))