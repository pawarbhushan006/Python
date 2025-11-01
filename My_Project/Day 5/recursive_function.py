# self calling function : function calls it self until certain condition is not met
#two parts of recursive function
#1. Base/terminal condition
#2. recursive condition

def factorial (n):
    if n == 0:
        return 1
    else:
        result =  n * factorial(n-1)
        return result

print(factorial(5))

#without recursion
def factorial_recursive(num):
    fact = 1
    while num>1:
        fact = fact * num
        num -= 1
    return fact

print(factorial_recursive(5))