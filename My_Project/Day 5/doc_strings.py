def func(num1,num2):
    """
    this is a docstring
    we can write what this function does
    num1 = which is numerator
    num2 = which is denominator
    :return:float
    """
    result = num1/num2
    return result

print(func(1,2))
print(help(func))

#docstring must be at start of function if we add post the code or anywhere else in code help() function will not work 