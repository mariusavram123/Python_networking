#!/usr/bin/python3

# Do not run this script - it serves as note

In [11]: "This is some string %s %s" % (my_var2, "ehlo")
Out[11]: 'This is some string Hello ehlo'

In [12]: "This is some string {} {}".format(my_var2, "ehlo")
Out[12]: 'This is some string Hello ehlo'

In [13]: f"This is some string: {my_var2} ehlo"
Out[13]: 'This is some string: Hello ehlo'
# Fstrings
In [14]: my_var3 = "ehlo"

In [15]: f"This is some string: {my_var2} {my_var3}"
Out[15]: 'This is some string: Hello ehlo'


In [16]: ip_addr1 = "10.220.89.17"

In [17]: print(f"F-strings allow me to embeed variables into a string: {ip_addr1}")
F-strings allow me to embeed variables into a string: 10.220.89.17



In [18]: print(f"F-strings technically allow expressions: {2 + 17}")
F-strings technically allow expressions: 19

In [20]: print(f"F-strings technically allow expressions: {ip_addr1.split(".")[0]}")
F-strings technically allow expressions: 10

In [21]: ip_addr2 = "192.168.1.1"

In [22]: ip_addr3 = "172.19.0.1"

# left oriented
In [23]: print(f"{ip_addr1:20}{ip_addr2:20}{ip_addr3:20}")
10.220.89.17        192.168.1.1         172.19.0.1          

# right oriented
In [24]: print(f"{ip_addr1:>20}{ip_addr2:>20}{ip_addr3:>20}")
        10.220.89.17         192.168.1.1          172.19.0.1

# Centered

In [26]: print(f"{ip_addr1:^20}{ip_addr2:^20}{ip_addr3:^20}")
    10.220.89.17        192.168.1.1          172.19.0.1     

# More tests

In [27]: header = "-" * 20

In [28]: header1 = "ip_addr1"

In [29]: header2 = "ip_addr2"

In [30]: header3 = "ip_addr3"

In [31]: print()


In [32]: print(f"{header1:^20}{header2:^20}{header3:^20}")
      ip_addr1            ip_addr2            ip_addr3      

In [33]: print(f"{header:^20}{header:^20}{header:^20}")
------------------------------------------------------------

In [34]: print(f"{header1:^20} {header2:^20} {header3:^20}")
      ip_addr1             ip_addr2             ip_addr3      

In [35]: print(f"{header:^20} {header:^20} {header:^20}")
-------------------- -------------------- --------------------

In [36]: print(f"{ip_addr1:^20} {ip_addr2:^20} {ip_addr3:^20}")
    10.220.89.17         192.168.1.1           172.19.0.1     

In [37]: print()


In [38]: my_var = 1/3

In [39]: my_var
Out[39]: 0.3333333333333333

In [40]: print(f"Value of my_var is :{my_var:.2f}")
# 2 = 2 digits
# f = floating number
Value of my_var is :0.33

In [41]: somevar = "hello"
# Print the variable and the value
In [42]: f"{somevar = }"
Out[42]: "somevar = 'hello'"

In [44]: f"Repr of somevar: {somevar!r}"
Out[44]: "Repr of somevar: 'hello'"




