#!/usr/bin/python3
# the default mode for opening a file is in read mode
f = open("show_version.txt")

print(f)

# read the entire content of the file as a string
#text = f.read()
#print(f"\n {text}")

# read the file line by line
# calling it again goes to the second line and so on
text1 = f.readline()

text2 = f.readline()

print(f" \n {text1} \n {text2}")

# go at the begining of the file
f.seek(0)

# read the entire content of the file as a string
data = f.readlines()

print(len(data))

print(type(data))

# loop over the content of the file:

for line in data:
    print(line)

f.close()