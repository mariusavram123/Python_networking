#!/usr/bin/python3
# get the version of the processor and board number

import re

with open("show_version3.txt","r") as f:
	data = f.read()

chasis = re.search("cisco (.*) processor", data, flags=re.M)

print(f"Chasis number: {chasis.group(1)}")

board = re.search("^Processor.*ID (.*)$", data, flags=re.M)

print(f"Processor board: {board.group(1)}")
