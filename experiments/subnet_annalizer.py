#!/usr/bin/python3
import sys

base_addr = "192.168.254."

prefix = int(input("Please enter a subnet mask between 25 and 32: "))

if not (prefix >= 25 and prefix <= 32):
    print("Invalid prefix ")
    sys.exit(1)

# The size of the subnet
subnet_size = 2 ** (32 - prefix)

subnets = 256 // subnet_size

print (f"Subnets: {subnets}")

hosts_size = subnet_size - 2

print(f"{subnet_size=}")

print(f"{hosts_size=}")

base_suffix = 0

for i in range(0,255,subnet_size):
    print(f"Network prefix: {base_addr}{str(base_suffix)}")
    print(f"First host: {base_addr}{str(base_suffix + 1)}")
    print(f"Last host: {base_addr}{str(base_suffix + hosts_size)}")
    print(f"Broadcast address: {base_addr}{str(base_suffix + hosts_size + 1)}\n\n")
    base_suffix += subnet_size