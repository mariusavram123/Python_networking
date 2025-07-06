#!/usr/bin/python3

import re

text = "Port Speed........................1000 full"

speed = re.match("Port Speed[.]+([0-9]+.*$)",text)
if speed:
    print(speed.group(1))
    print("Matches")
else:
    print("Not matches")