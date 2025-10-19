from fstring_python import language

s1 = "Python is Fun"

print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "1.0.0"
print(language + version)

# in string '*' is repetition operator
print(language*3)

# membership operation
#in : to check given string is part of existing string or not
print("Python" in s1)
print("z" in s1)
#not in
print("z" not in s1)
print("Python" not in s1)

# comparision
print("Python is Fun" == s1)
print("Pythonis Fun" == s1)

# remove space from string starting and end spaces
s1= " Python "

print(s1.strip()=="Python")

#replace
s1 = "Hello Python!"
print(s1.replace("Python", "Java",1))

# counting substring in string , can be used get count of character
# string.count()

s1="python is fun. We are learning Python"
print(s1.replace("Python", "Java",1))
print(s1.count("Python"))

#chage case of string
#upper(), lower(), title(), capatilize()

print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
print(s1.swapcase())

# startswith(): to check string starts with any substring
#string.startswith(substring)
print(s1.startswith("python"))

#endswith()\
print(s1.endswith("Python"))


