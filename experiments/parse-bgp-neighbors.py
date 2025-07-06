#!/usr/bin/python3
# parse the show ip bgp neighbors output

import re

with open("show_ip_bgp_neighbors.txt", "r") as f:
    data = f.read()


neighbor = re.search("^BGP neighbor is ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+),.*AS ([0-9]+),", data, flags=re.M)

ip = neighbor.group(1)

remote_as = neighbor.group(2)

print(f"Neighbor IP: {ip}\nRemote as: {remote_as}")

bgp_info1 = re.search("BGP version ([0-9]), remote.*ID (.*)$", data, flags=re.M)

bgp_ver = bgp_info1.group(1)

bgp_remote_id = bgp_info1.group(2)

print(f"BGP version: {bgp_ver}\nRemote router: {bgp_remote_id}")

bgp_info2 = re.search("BGP state = (.*),.*$", data, flags=re.M)

bgp_state = bgp_info2.group(1)

print(f"Connection state: {bgp_state}")
