#local variable: created within function and accessible within function
#global variable: defined outside of function and accessible anywhere in program
test = 25 #global variable
def func ():
    age = 20 #local variable
    print(f"inside the function {age}")
    print(f"inside the function {test}")
    print(f"inside the function {test2}")

test2 = 50 # we can define global variable anywhere in program except insight function\
age =100
func()

#print(f"outside the function{age}") : this will not work as age is local variable
print(f"outside the function {test}")
print(f"outside the function {test2}")
print(f"outside the function {age}")

#if we want to edit global variable value inside the function we need to use global keyword
#without global keyword function cant use global variable version inside the function

def func2():
    global test3
    test3 += 1
    print(f"inside the function {test3}")
test3 = 0
func2()