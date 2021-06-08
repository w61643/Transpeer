#print("1")
from typing import get_args


x = 3
#print(x-1)
#print(type(x))
"""object of type 'int' has no len()"""
#print(len("x-1")) 

thislist = ["apple", "banana", "cherry"]
#print(thislist)

thislist = ["apple", "banana", "cherry"]
#print(thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
#print(thislist)

thislist = ["apple", "banana", "cherry"]
#for x in thislist: print(x)

thislist = ["apple", "banana", "cherry",1]
#if 1 in thislist: print("Yes, 1 is in the fruits list")

thislist = ["apple", "banana", "cherry",1]
#print(len(thislist))

thislist = ["apple", "banana", "cherry"]
"""takes exactly one argument """
thislist.append(1.1)
#print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(21, "orange")
#print(id(thislist))

