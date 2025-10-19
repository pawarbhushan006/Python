#mutability and immutability
from ctypes import pythonapi

#list are mutable
#tuples and strings are immutable

s1 = "Python is Fun"
s1.replace("Python", "Java") #this will not edit the existing string
s2=s1.replace("Python", "Java")
print(s1)
print(s2)
print(s1.split())

#list ::
t1 = ["mango","orange","apple"]
t1.append("banana")
print(t1)
#to check memory address we use id()
print(id(t1))
#reassignment of value

l1 = ["mango","orange","aple"]
l1[-1]="apple"
print(l1)

#adding new value and reassignment of value in tuples and strings not possible

#sets are multable but frozen sets are mutable
#dict are mutable
