#!/usr/bin/python3
# parse aruba cx show ipv6 intf output

import re

with open("aruba_cx_show_ipv6_intf.txt", "r") as f:
    output = f.read()

# get interface name, interface state, admin state and ipv6 address

name_state = re.search("^Interface (.{5}) is (.*)\n", output, flags=re.M)
if name_state:
    name = name_state.group(1)
    state = name_state.group(2)
    print(f"Interface {name} status {state}")

admin_state = re.search("Admin state is (.+)\n", output, flags=re.M)
if admin_state:
    print(f"Admin state: {admin_state.group(1)}")

search = r"[0-9a-f]{4}"

ipv6_address = re.search("IPv6 address:\n\s{3}(.*/24) \[V", output, flags=re.M)

if ipv6_address:
    print(f"IPv6 address: {ipv6_address.group(1)}")
