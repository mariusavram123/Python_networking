#!/usr/bin/python3
# interface class

class Interface:

    def __init__(self,
                 intf_name,
                 intf_mode="access",
                 access_vlan=None,
                 speed="1Gbps",
                 duplex="full"):

        self.intf_name = intf_name
        self.intf_mode = intf_mode
        self.access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex
        # lower the intf mode if we got it with caps
        self.intf_mode = self.intf_mode.lower()

        if self.intf_mode not in ["access", "trunk"]:
            raise ValueError("Only access or trunk modes allowed for an interface")

        if self.intf_mode == "access" and self.access_vlan is not None:
            try:
                self.access_vlan = int(self.access_vlan)
                if self.access_vlan < 0 or self.access_vlan > 4094:
                    raise ValueError("Incorrect VLAN ID. Please provide a number between 0 and 4094")
            except:
                raise ValueError("Cannot convert the access vlan to integer")
        elif self.intf_mode == "access" and self.access_vlan is None:
            raise ValueError("An interface in access mode should have a correct access vlan ID")
        elif self.intf_mode == "trunk":
            # turn access vlan to None if the interface is trunk
            self.access_vlan = None

    def __str__(self):
        return f"Interface: {self.intf_name}, ({self.speed}, Mode: {self.intf_mode}, VLAN: {self.access_vlan})"


e1 = Interface(intf_name="1/1", intf_mode="access", access_vlan=34)

e2 = Interface(intf_name="1/2", intf_mode="access", access_vlan=44)

e3 = Interface(intf_name="2/3", intf_mode="trunk")

e4 = Interface(intf_name="3/4", intf_mode="access", access_vlan=85)

e5 = Interface(intf_name="8/5", intf_mode="trunk", access_vlan=1921)

e6 = Interface(intf_name="eth3", intf_mode="access", access_vlan=85, speed="100Mbps")

e7 = Interface(intf_name="eth4", intf_mode="access", access_vlan=4090, speed="1000Mbps", duplex="half")

for item in [e1, e2, e3, e4, e5, e6, e7]:
    print(item)
