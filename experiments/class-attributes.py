#!/usr/bin/python3

# global class attributes


class TelnetConn:
    # class atribute - number of connections
    conns = 0

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        # initiate telnet connections
        self.open()

    def open(self):
        """Create telnet connection"""
        self.telnet_conn = f"Telnetting to {self.host}"
        self.login()
        TelnetConn.conns += 1
        print(f"Number of telnet connection: {self.conns}")
        # if conns attribute is not on the object,
        # then it is looking on the class attributes
