#!/usr/bin/python3
import re

with open("arista_show_ip_arp.txt", "r") as f:
    data = f.read()

arp_table = re.findall("([0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}).*([0-9a-f]{4}[.][0-9a-f]{4}[.][0-9a-f]{4}).*V", data)

if arp_table:
    arp_data = dict(arp_table)
    print(arp_data)
