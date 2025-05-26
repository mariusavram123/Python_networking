#!/usr/bin/python3

# Udev interface renamer written in python

import sys
import subprocess
#import os
import getpass
from pathlib import Path

user = getpass.getuser()
print("The current user is: " + user)

#verify that we run the script as root, if not exit with code 17
if user != "root":
    print("Please run the script as root or with sudo privileges.")
    sys.exit(17)

def show_usage():
    print("Usage: " + sys.argv[0] + " current_interface new_interface")
    print("Renames the current interface to the new interface. Current interface and new interface should not have '.' or ':' in the name")
    print(sys.argv[0] + ": Prints this help menu and exit")

if len(sys.argv) == 1:
    print("Too less arguments.")
    #show_usage()
    #sys.exit(17)

if len(sys.argv) != 3:
    print("This script expects exactly 2 positional arguments.")
    show_usage()
    sys.exit(17)

# initialize the variables
current_interface = sys.argv[1]
new_interface = sys.argv[2]

# verifying that it is a correct interface name, existing on the system
def verifyinterface(current_interface):
    # Make sure we got an ethernet interface or wifi interface, no loopback allowed(this also excludes loopback interfaces)
    if not (current_interface.startswith("e") or current_interface.startswith("w")):
        print("Interfaces tha are not ethernet or wireless are not allowed to be renamed.")
        sys.exit(17)

    # every interface haves a file in /sys/class/net/
    interface_status = Path("/sys/class/net/" + current_interface)
    if not interface_status.is_file():
        #print(interface_status)
        print("The interface you want to rename does not exist. Exiting")
        sys.exit(17)

    # do not allow alias
    if ":" in current_interface:
        print("We do not accept an alias in the interface name. Only the parrent interface accepted")
        sys.exit(17)

    # do not allow VLAN
    if "." in current_interface:
        print("Please specify the interface name without the VLAN ID. Only the parrent interface allowed.")
        sys.exit(17)


verifyinterface(current_interface)

# Rename the interface to the new name
def rename_interface(current_interface,new_interface):
    file = "/etc/udev/rules.d/59-persistent-net.rules"
    print("Finding the interface's PCI ID")
    interface_info = subprocess.check_output("/usr/sbin/udevadm info -a -p /sys/class/net/" + current_interface + "| grep 'KERNEL'", shell = True)
    pci_id = list(interface_info.split())
    kernel_id = pci_id[2]
    kernel = str(kernel_id)[1:].replace("'","")
    with open(file, 'a') as f:
        f.write("# Renaming " + current_interface + " to " + new_interface + "\nSUBSYSTEM==\"net\", ACTION==\"add\", " + kernel + ", NAME:=\"" + new_interface +"\"")
        #f.read()
    string_info = subprocess.check_output("cat " + file, shell = True)
    print(string_info)

rename_interface(current_interface,new_interface)

#def set_interface_name(current_interface, new_interface):
    # if nmcli is installed proceed using nmcli
#    nmcli = Path("/usr/bin/nmcli")
#    if nmcli.is_file():
#        print("Modifying the interfaces from nmcli connections.\n")
#        connnection = subprocess.check_output("nmcli device show " + current_interface + "|grep GENERAL.CONNECTION", shell = True)
#        conn_id = list(connection.split())
#        print (conn_id)

#set_interface_name(current_interface,new_interface)

print("Please manually modify the nmcli interfaces using the following command: 'nmcli connection modify <current_interface_name> connection.interface-name " + new_interface + "'")
print("The new name will be taken by the interface after a system reboot.")
print("Please verify that everything is ok on the file.")
