from scapy.all import *
from scapy.contrib.igmpv3 import IGMPv3, IGMPv3gr, IGMPv3mr
from scapy.layers.inet import IPOption_Router_Alert
# from scapy.contrib.mpls import MPLS

iface = "enp2s0"

# Multicast group to join
group_ip = "239.1.1.1"

# Ethernet multicast MAC for 224.0.0.22
igmp_mac = "01:00:5e:00:00:16"

# IGMPv3 Group Record (ASM join)
# rtype = 1 MODE_IS_INCLUDE
# rtype = 2 MODE_IS_EXCLUDE
group_record = IGMPv3gr(
    rtype=2,        # MODE_IS_EXCLUDE
    maddr=group_ip,
    srcaddrs=['172.16.29.234']
)

# IGMPv3 Membership Report
igmp_report = IGMPv3mr(
    records=[group_record]
)

igmp = IGMPv3(type=34)

# mpls = (
#     MPLS(label=18, cos=1, s=0, ttl=1) / MPLS(label=20, s=0, ttl=1) /
#     MPLS(label=80, cos=2, ttl=1) / MPLS(label=21, cos=0, s=1, ttl=1)
# )

# Full packet (Ethernet + IP + IGMP)
pkt = (
    Ether(dst=igmp_mac) /
    IP(dst="224.0.0.22", ttl=1, options=[IPOption_Router_Alert()]) /
    igmp / igmp_report
)

pkt.show2()

# Send at layer 2
sendp(pkt, iface=iface, verbose=True)
