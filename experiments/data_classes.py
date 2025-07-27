#!/usr/bin/python3

# data classes in python
# python does not enforce data type by default

from dataclasses import dataclass


@dataclass
class NetDevice:
    host: str
    username: str
    password: str
    # specify default value
    # only allowed when all nondefault attributes were defined
    # so device_type goes at the end
    device_type: str = "cisco_ios"


rtr1 = NetDevice(
        device_type="Juniper JUNOS",
        host="rtr1.local",
        username="marius",
        password="jnpr123"
)

print(rtr1.device_type)
print(rtr1.host)
