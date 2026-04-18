from   scapy.all import *
from   scapy.contrib.lldp import *
import socket
import sys
import random
import time

# 
# LLDP PDU generator - please use responsibly! 
#
# author: cpaggen, Jan 2025
#

iface = "bridge0"

# set your NIC's MAC here
src_mac          = get_if_hwaddr(iface)
# modify as you see fit
dst_mac          = "01:80:c2:00:00:0e"
port_id          = iface
pdu_ttl          = 120
mgmt_ip          = get_if_addr(iface)
remote_host_name = "fedora43"
remote_host_desc = "Linux fedora43 6.19.10-200.fc43.x86_64"
port_description = "Bridge 0"
capabilities = {
    # Available Capabilities
    'router_available': 1,
    'mac_bridge_available': 1,
    'other_available': 1,
    'telephone_available': 0,
    'reserved_5_available': 0,
    'two_port_mac_relay_available': 0,
    's_vlan_component_available': 1,
    'c_vlan_component_available': 1,
    'station_only_available': 1,
    'docsis_cable_device_available': 1,
    'wlan_access_point_available': 0,
    'repeater_available': 0,
    'reserved_1_available': 1,

    # Enabled Capabilities
    'router_enabled': 1,
    'mac_bridge_enabled': 1,
    'other_enabled': 1,
    'telephone_enabled': 0,
    'two_port_mac_relay_enabled': 0,
    's_vlan_component_enabled': 1,
    'c_vlan_component_enabled': 1,
    'station_only_enabled': 1,
    'docsis_cable_device_enabled': 1,
    'wlan_access_point_enabled': 0,
    'repeater_enabled': 0,
}
org_code         = 0x000555  
org_subtype      = 0x66       
org_data         = b'SC.Marius.SRL'

def generateRandomSystemName():
    adjectives = [
    "Avian",
    "Feathered",
    "Winged",
    "Soaring",
    "Warbling",
    "Colorful",
    "Bright",
    "Vibrant",
    "Graceful",
    "Elegant",
    "Slender",
    "Sturdy",
    "Robust",
    "Small",
    "Tiny"
    ]
    birds = [
    "Robin",
    "Blue Jay",
    "Cardinal",
    "Owl",
    "Eagle",
    "Hawk",
    "Hummingbird",
    "Pigeon",
    "Crow",
    "Sparrow",
    "Woodpecker",
    "Swan" 
    ]
    randomAdjective = random.choice(adjectives)
    randomBird      = random.choice(birds)
    return f"{randomAdjective} {randomBird}"

def generateRandomMac():
  # set first octet to zero to avoid multicast MAC, just in case
  mac = [0x00]
  mac.append(random.choice([0x00, 0x02, 0x04, 0x06, 0x08, 0x0A, 0x0C, 0x0E]))
  for _ in range(4):
      mac.append(random.randint(0, 255))

  return ':'.join(['{:02x}'.format(x) for x in mac])

def craftLLDPDU():
    # Create the LLDP frame one TLV at a time
    _chassis_id         = LLDPDUChassisID(subtype=0x04, id=src_mac)
    _port_id            = LLDPDUPortID(subtype=7, id=port_id)  
    _ttl                = LLDPDUTimeToLive(ttl=pdu_ttl)
    _port_description   = LLDPDUPortDescription(description=port_description)
    _system_name        = LLDPDUSystemName(system_name=remote_host_name)
    _system_description = LLDPDUSystemDescription(description=remote_host_desc)
    _system_cap         = LLDPDUSystemCapabilities(**capabilities)
    _mgmt_address       = LLDPDUManagementAddress(management_address_subtype=1, management_address=socket.inet_aton(mgmt_ip))
    _org_spec_tlv       = LLDPDUGenericOrganisationSpecific(org_code=org_code,subtype=org_subtype,data=org_data)
    _end_of_lldp        = LLDPDUEndOfLLDPDU()

    lldpu_layer = (
      _chassis_id 
    / _port_id 
    / _ttl 
    / _system_name 
    / _system_description 
    / _port_description 
    / _mgmt_address 
    / _system_cap 
    / _org_spec_tlv 
    / _end_of_lldp
    ) 

    packet = lldpu_layer
    return packet

def main(numPDUs):
    ether_layer = Ether(src=src_mac, dst=dst_mac)
    # vlan_layer = Dot1Q(vlan=777, type=0x88cc)
    for pdu in range(numPDUs):
        lldp = craftLLDPDU()
        packet = ether_layer / lldp
        # the kernel already encapsulates in dot1q because eno6.777 is a VLAN subinterface
        # as such no need to add vlan_layer to the packet but do experiment with your setup
        packet.show2()
        sendp(packet, iface=iface)
        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <number_of_LLDP_PDUs>")
    numPDUs = int(sys.argv[1])
    main(numPDUs)
