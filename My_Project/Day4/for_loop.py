"""
for loop: Used for definite iteration. This means you know beforehand how many
times you want to loop, or you want to process each item in a collection (like a list or
string). It "iterates over" a sequence of items.

"""

percents = [85.5, 95.5, 100, 10.5]
for var in percents:
    print(var)
s1= "Hello World"

for char in s1:
    print(char)
print("end of loop")

employee = {'name':'John','age':25, 'ID': 123456}
for key in employee:
    print(key,employee[key])
for val in employee.values():
    print(val)
for val in employee.items():
    print(val)
print('test')
for i in employee.items():
    print(i[0],i[1]) # i[0] : pointing to key and i[1]: pointing to value





