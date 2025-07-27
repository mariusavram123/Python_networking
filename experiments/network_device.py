#!/usr/bin/python3

# a networkdevice class

from getpass import getpass


class NetworkDevice:

    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        self.password = password

        if password is None:
            self.password = getpass(f"Please provide a password for {self.host}: ")

    def __str__(self):
        return f"{self.host}, ({self.platform})"


cisco = NetworkDevice(host="cisco1.lan", platform="cisco-ios",
                      username="admin", password=None)

arista = NetworkDevice(host="arista1", platform="arista-eos",
                       username="arista", password="Test123!")

juniper = NetworkDevice(host="junos1.router.local", platform="juniper-junos",
                        username="junadmin", password=None)
print(cisco)

print(arista)

print(juniper)
