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

# string membership

In [1]: some_str = "It was the best of times, it was the worst of times."

In [2]: "the best" in some_str
Out[2]: True

# Raw strings

In [5]: some_other_str = "What is\new in this\time?"

In [6]: some_other_str
Out[6]: 'What is\new in this\time?'

In [7]: win_path = "c:\windows\new_dir\test\applications"

In [8]: print(win_path)
c:\windows
ew_dir  estpplications

In [9]: print(some_other_str)
What is
ew in this      ime?

In [10]: win_path = r"c:\windows\new_dir\test\applications"

In [11]: print(win_path)
c:\windows\new_dir\test\applications

# string concatenation

In [12]: city = "San Francisco"

In [13]: state = "CA"

In [14]: location = city + ", " + state

In [15]: location
Out[15]: 'San Francisco, CA'

In [16]: 


# string concatenation with += operator

In [16]: data = "line 1 of some output\n"

In [17]: data = data + "line 2 of some output\n"

In [18]: print(data)
line 1 of some output
line 2 of some output


In [19]: new_data = "line 1 of some output\n"

In [20]: new_data += "line 2 of some output\n"

In [21]: print(new_data)
line 1 of some output
line 2 of some output

# strings - ordered lists of characters

In [22]: my_var = "some string"

In [23]: my_var[0]
Out[23]: 's'

In [24]: my_var[1]
Out[24]: 'o'

In [25]: my_var[2]
Out[25]: 'm'

In [26]: for letter in my_var:
    ...:     print(letter)
    ...: 
s
o
m
e
 
s
t
r
i
n
g

# length of the string

In [27]: len(my_var)
Out[27]: 11



In [40]: print(f"{header1:^20} {header2:^20}")
       sf_gw1               sf_gw2       

In [41]: print(f"{header:^20} {header:^20}")
-------------------- --------------------

In [42]: print(f"{sf_gw1:^20} {sf_gw2:^20}")
  172.31.255.1/24      10.254.1.252/24   

# Numbers:

In [1]: my_var = 22

In [2]: type(my_var)
Out[2]: int

In [3]: 17 + 22
Out[3]: 39

In [4]: 22 - 7
Out[4]: 15

In [5]: 3 * 4
Out[5]: 12

In [6]: 4 / 7
Out[6]: 0.5714285714285714

In [7]: 


# modulo operator

In [7]: my_var = 9

In [8]: my_var % 2
Out[8]: 1

In [9]: my_var % 3
Out[9]: 0

In [10]: 

# raising to the power:

In [10]: 2 ** 3
Out[10]: 8

In [11]: 2 ** 4
Out[11]: 16

In [12]: 2 ** 5
Out[12]: 32

# floats

In [13]: my_var = 3.3

In [14]: type(my_var)
Out[14]: float

In [15]: 3.3 + 2.7
Out[15]: 6.0

In [16]: 7 / 2
Out[16]: 3.5

In [17]: 3.1 * 2.5
Out[17]: 7.75

# Rounding floats

In [20]: my_var = 4 / 3

In [21]: my_var
Out[21]: 1.3333333333333333

In [22]: round(my_var, 2)
Out[22]: 1.33

# incrementing counters

In [23]: i = 0

In [24]: i = i + 1

In [25]: i
Out[25]: 1

In [26]: i += 1

In [27]: i
Out[27]: 2

In [28]: i += 1

In [29]: i
Out[29]: 3

# decrement counters

In [29]: i
Out[29]: 3

In [30]: i -= 1

In [31]: i
Out[31]: 2

# booleans and None

In [32]: my_var = True

In [33]: type(my_var)
Out[33]: bool

In [34]: my_var2 = False

In [35]: type(my_var2)
Out[35]: bool


In [36]: my_value = None

In [38]: val1 = True

In [39]: val2 = False

In [40]: if val1 and val2:
    ...:     print("Hello")
    ...: 

In [41]: if val1 or val2:
    ...:     print("World")
    ...: 
World

In [42]: if my_value is None:
    ...:     print("Whatever")
    ...: 
Whatever


In [44]: my_var1 = True

In [45]: my_var2 = True

In [46]: my_var1 and my_var2
Out[46]: True

In [47]: my_var2 = False

In [48]: my_var1 and my_var2
Out[48]: False

In [49]: my_var1 or my_var2
Out[49]: True


In [50]: not my_var2
Out[50]: True

# truish


In [51]: if "some_string":
    ...:     print("Hello")
    ...: 
Hello

In [52]: if 22:
    ...:     print("Hello")
    ...: 
Hello


In [53]: if my_var1:
    ...:     print("Hello something")
    ...: 
Hello something

In [54]: if my_var == True:
    ...:     print("Hello something")
    ...: 
Hello something

In [55]: if my_var1 is True:
    ...:     print("Hello something")
Hello something

In [56]: my_var1 = "some string"

In [57]: 

In [57]: type(my_var1)
Out[57]: str

In [58]: if my_var1:
    ...:     print("Hello")
Hello

In [59]: my_var1 = ""

In [60]: if my_var1:
    ...:     print("Not false")
    ...: 

# the empty string is evaluated as being false, every other string is considered true


In [61]: bool(my_var1)
Out[61]: False

In [62]: my_var1 = "every other string"

In [63]: bool(my_var1)
Out[63]: True

# integer 0 is going to be mapped to bool false

In [64]: my_var1 = 0

In [65]: bool(my_var1)
Out[65]: False

# every other integers will be evaluated as true

In [66]: bool(-75)
Out[66]: True

In [67]: my_var1 = 42

In [68]: bool(my_var1)
Out[68]: True

# the empty list is evaluated as false

# every other list is evaluated as true

In [69]: my_var1 = []

In [70]: bool(my_var1)
Out[70]: False

In [71]: my_var1 = ["a", "b", "c"]

In [72]: bool(my_var1)
Out[72]: True


# the nonetype

In [73]: my_var1 = None

In [74]: type(my_var1)
Out[74]: NoneType

In [75]: bool(my_var1)
Out[75]: False

