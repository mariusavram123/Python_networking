#!/usr/bin/python3

# Network interfaces configurator written in python
# ssh on the vm and create the interfaces

# usage: ./network_conf.py interface_type vlan_id(in case of vlans) physical_interface

import paramiko
import time
import re
import sys

hostname = input("Please enter the IP address or host name to connect to: ")

username = input("Enter your username: ")

port = input("Please enter the ssh port number. Default: 22 ")

def show_usage():
	print("Usage: " +sys.argv[0] + "interface_type vlan_id parrent_interface")
	print(sys.argv[0] + " -h | --help: Print this help menu and exit")
	sys.exit(0)

if len(sys.argv) != 4:
	print("Not enough arguments. Exiting... ")
	show_usage()
	sys.exit(17)

interface_type = sys.argv[1]

vlan_id = sys.argv[2]

physical_interface = sys.argv[3]

if ((type(port) != "int") and (port == "")) :
    print("Using default port 22. ")
    port = 22

# verify that the user entered an valid ip address
def isvalidip(hostname):
    if re.match("^.{1,3}[.].{1,3}[.].{1,3}[.].{1,3}",hostname):
        print("This is a valid IP address. ")
    else:
        print("Invalid IP address. Stopping the script. ")
        sys.exit(17)

isvalidip(hostname)

def getnetinterfacenames():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname, username = username, port = port, key_filename = "/home/marius/.ssh/id_rsa", password = "")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ip address")
    ssh_stdin.close
    time.sleep(1)
    output = ssh_stdout.read()
    # extract the lines from the output
    out = output.splitlines(keepends=False)
    # print the first and the 5th line of the string - containing interface names
    #print(out[0] + out[6])
    #print(output)
    #print(ssh_stderr.read())
    output = out[0].split()
    #print(output.split())
    #print(output[1][2:len(output[1] - 1)])
    fulliface1 = output[1]
    ifacestr = str(fulliface1)
    print("Found first interface " + ifacestr[2:-2])
    output2 = out[6].split()
    fulliface2 = output2[1]
    iface2 = str(fulliface2)
    print("Found the second interface " + iface2[2:-2])
    ssh.close

getnetinterfacenames()
