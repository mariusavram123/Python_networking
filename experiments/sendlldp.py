from scapy.all import *

# LLDP multicast destination MAC
LLDP_DST_MAC = "01:80:c2:00:00:0e"

# Your interface
iface = "bridge0"

# Build LLDP TLVs manually
def lldp_tlv(tlv_type, value):
    length = len(value)
    tlv_header = (tlv_type << 9) | length
    return tlv_header.to_bytes(2, byteorder='big') + value

# Chassis ID TLV (type 1)
chassis_id = lldp_tlv(1, b'\x04' + b'00:11:22:33:44:55')

# Port ID TLV (type 2)
port_id = lldp_tlv(2, b'\x05' + b'bridge0')

# Time To Live TLV (type 3)
ttl = lldp_tlv(3, (120).to_bytes(2, byteorder='big'))

# End of LLDPDU TLV (type 0)
end = b'\x00\x00'

# Combine LLDP payload
lldp_payload = chassis_id + port_id + ttl + end

# Build Ethernet frame
frame = Ether(dst=LLDP_DST_MAC, type=0x88cc) / Raw(load=lldp_payload)

# Send packet
sendp(frame, iface=iface, verbose=True)
