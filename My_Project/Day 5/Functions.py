# def my_function(para1, para2,..):
#     statement 1
#     statemet 2
#def of function
def greeting_someone(name):
    print(f"Hello {name}!")

#calling function
greeting_someone('Bhushan')

def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(10)
even_odd(1245)

def add(num1, num2):
    return num1 + num2

print(add(2, 3))

def arithmetic(num1, num2):
    add_1 = add(num1, num2)
    sub_1 = num1-num2
    mul_1 = num1*num2
    div_1 = num1/num2
    return add_1, sub_1, mul_1, div_1

num1 = int(input('Enter a value 1:'))
num2 = int(input('Enter a value 2:'))

res1,res2,res3, res4 = arithmetic(num1,num2)

print(f"Addition of {num1} and {num2} is {res1}")
print(f"Subtraction of {num1} and {num2} is {res2}")
print(f"Multiplication of {num1} and {num2} is {res3}")
print(f"Division of {num1} and {num2} is {res4}")