#!/usr/bin/python3
import re

f = open("show_version2.txt", mode="r")

data = f.read()

line = data.splitlines()[1]


# lowercase \s matches white space
patt1 = re.search("Cisco\s.*[fF]uji", line)

print(patt1.group(0))

alt_line = "Cisco        Fuji"

# uppercase \S matches non white space
# \w - word character class
patt2 = re.search("\w+\s+[fF]uji", alt_line)

print(patt2.group(0))

# \d means search for decimal characters
patt3 = re.search("^Cisco.*(\d\d\.\d\.\d).*$", line)

print(patt3.group(0))
print(patt3.group(1))

patt4 = re.search("^Cisco.*ion ([\d\.]+), REL", line)

print(patt4.group(0))
print(patt4.group(1))

# print(data)
# re.MULTILINE can be abbreviated as re.M
patt5 = re.search("^Configuration register is (\S+)$", data, flags=re.M)
print(patt5.group(0))
print(patt5.group(1))

# by default the . character does not match the new line (\n)
# re.DOTALL changes this behaviour, re.DOTALL can be shorted as re.D
patt6 = re.search("^.*$","simple test\nhello", flags=re.DOTALL)
print(patt6.group(0))

# ?P - named pattern matching - you can use the groupdict method or retrieve the group with name captured
patt7 = re.search("^Configuration register is (?P<confreg>\S+)$", data, flags=re.M)
print(patt7.groupdict())
print(patt7.group("confreg"))

f.close()
