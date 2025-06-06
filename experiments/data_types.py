#!/usr/bin/python3

# Playing with data types in python

# string
a = "test"
print("A is " + str(type(a)))

# integer
b = 123
print ("B is " + str(type(b)))

# float
c = 1.25
print("C is " + str(type(c)))

# list - you can append
alist = ["mere", "pere", "banane"]
print(type(alist))
# add an element to list
alist.append("rosii")
print(alist)
# remove an element from list
alist.remove("pere")
print(alist)
# get the position of a element
print(alist.index("banane"))
# modify a value of a string in list
alist[1] = "cireasa"
print(alist)

# tuple
atuple = ("ana", "are", "mere")
print(type(atuple))

# dictionary
adict = {"name": "marius", "age": 30}
# print the value of an element of an array
print(adict["name"])
# add element to dictionary
adict["job"] = "none"
print(adict)
# update the value of an item in dictionary
adict.update({"age": 33})
adict.update({"job": "maybe"})
print(adict)
# add an item to dictionary
adict.update({"brother": "Emil"})
print(adict)
# remove item from dictionary
adict.pop("job")
print(adict)

# loop through the items of a dictionary
# print only the keys
for x in adict:
    print(x)

# print only the values
for x in adict:
    print(adict[x])
adict.pop("brother")
adict["brother1"] = {"name": "Emil", "age": 20}
adict["brother2"] = {"name": "Mihai", "age": 30}
print(adict)
brothers = (adict["brother1"], adict["brother2"])
print(brothers)
# tuple of dictionaries
print(type(brothers))
# list of dictionaries
brothers = [adict["brother1"], adict["brother2"]]
print(type(brothers))

# tupple added to list - result list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(type(thislist))

# list added to tuple dont work - cannot add items to tuple
#thislist = ("apple", "banana", "cherry")
#thistuple = ["kiwi", "orange"]
#thislist.extend(thistuple)
#print(type(thislist))

x = 3
y = 4

def summ(x, y):
    print(x + y)

summ(x, y)

def diff(x , y):
    print(x - y)

diff(x, y)

def power(x, y):
    print(x**y)

power(x,y)

def multi(x, y):
    print(x*y)

multi(x,y)

def div(x,y):
    if y == 0:
        print("You cannot make division by 0")
        return False
    print(x / y)

div(x,y)

def modul(x, y):
    if y == 0:
        print("You cannot make module division by 0")
        return False
    print(x % y)

modul(x,y)

def floordiv(x,y):
    if y == 0:
        print("You cannot make floor division by 0")
        return False
    print(x//y)

floordiv(10,y)
