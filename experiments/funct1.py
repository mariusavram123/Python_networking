#!/usr/bin/python3
# You can pass a list as a parameter to a function to replace all
# the necessary parameters needed for the function using *variable notation
# (* = args)

# from telnetlib import Telnet
from socket import gethostbyname


def print_ips(ip_addr1, ip_addr2):
    print(f"{ip_addr1=}")
    print(f"{ip_addr2=}")


sf_addresses = ["10.1.1.1", "10.1.1.2"]

print_ips(*sf_addresses)

print("\n")
# Passing arguments using dictionaries - pass named arguments

ips = {
    "ip_addr1": "192.168.100.1",
    "ip_addr2": "192.168.100.2",
    }

print_ips(**ips)


# using args as function arguments
# use *args to pass any number of parameters

def show_ips(*args):
    """Can take any number of arguments"""
    print(type(args))
    print(args)


show_ips("10.1.1.1", "10.15.1.2", "172.16.192.8")

# Pass any number of keyword arguments to a function(named)


def show_ips2(**kwargs):
    print(type(kwargs))
    print(kwargs)


show_ips2(
    ip_addr1="10.1.1.1",
    ip_addr2="10.200.15.30",
    ip_addr3="192.168.15.33"
)


# self._username - private attribute - internal to the class
# The developer wanted to make this parameter only internal to the class

# self.__address - name mangling - like hiding the name in the class
# not very commonly used

# accessing a name mangling attribute:
# nd._NetDevice,__device_type

class NetDevice:
    def __init__(self, device_type, host, username, password, port=22):
        # name mangling
        self.__device_type = device_type
        self.host = host
        # private attributes
        self._username = username
        self._password = password
        self.port = port

    def __str__(self):
        return f"NetDevice Object {self.host}:{self.port}"


nd = NetDevice(
    host="test1.local",
    device_type="cisco_ios",
    username="marius",
    password="cisco123",
    port=22
)

# import pbdr
# pbdr.set_trace()

# print(nd.username)
# calling the private attribute
print(nd._username)

# calling name mangled parameter
print(nd._NetDevice__device_type)

# dunder methods are like __init__ or __str__...
# calling the object of the class itself
# will return the __str__ method
print(nd)


class TelnetHost:
    def __init__(self, host, username, password):
        # get hello world to be printed out once we access the host attribute
        self._host = host
        self.username = username
        self.password = password
        self.telnet_conn = f"Telnetting to {self._host}"

    # property is a decorator
    @property
    def host(self):
        print("Hello World")
        return self._host

    # setters for parameters values
    # use @property.setter
    @host.setter
    def host(self, value):
        print(f"Setting host to {value}")
        self._host = value

# commented this to not rewrite all class
    # def get_host(self):
    #     print("Hello World")
    #     return self._host
    #
    # def set_host(self, value):
    #     self._host = value


tc = TelnetHost(
        host="test.com",
        username="marius",
        password="cisco123",
)

# print(tc.get_host())
# tc.host = "Testdevice1"

# this method does not change it internally
# and the code can be a mess because of getters and setters
print(tc.host)
print(tc._host)

tc.host = "Marius.router.lan"

print(tc.host)
# alternate solution is to use the @property
# create a method with the name you want to change
# the behaviour for it

# update the telnet connection to the host once we are changing it


@property
def host(self):
    return self._host


@host.setter
def host(self, value):
    if value != self._host:
        ip_addr = gethostbyname(value)
        self._host = value
        print(ip_addr)
        del self.telnet_conn
        self._open()


def _open(self):
    """Create a new telnet connection"""
    self.telnet_conn = f"Telnetting to {self._host}"
    self.login()
# a deleter for an attribute


@host.deleter
def host(self):
    print("Deleting host attribute")
    del self._host

# del tc.host
