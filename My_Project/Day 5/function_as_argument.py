# we can pass function as an argument of another function
def add_1(num1):
    return num1 + 1

print(add_1(2))

def square(x):
    return x ** 2
print(square(3))

num = int(input("Input a number"))

res2 = square(add_1(num))

print(res2)