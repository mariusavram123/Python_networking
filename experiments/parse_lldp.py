#!/usr/bin/python3

import re

with open("show_lldp.txt", "r") as f:
    lldp_data = f.read()

pattern = re.findall("Chassis id.*?Vlan ID", lldp_data, flags=re.M | re.DOTALL)

# print(pattern)

for item in pattern:
    text = item.split("\n")
    for line in text:
        local_port = re.search("^Local Port id: (.*)$", line)
        if local_port:
            print(f"Local port id: {local_port.group(1)}")
        remote_system = re.search("^System Name: (.*)$", line)
        if remote_system:
            print(f"Remote system: {remote_system.group(1)}")
        remote_port = re.search("^Port id: (.*)$", line)
        if remote_port:
            print(f"Remote port id: {remote_port.group(1)}")
    print("\n")
