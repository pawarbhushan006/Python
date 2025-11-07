
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError as error:
    print("Division not allowed by zero")
    print(error)
except ValueError:
    print("in correct number!")
else: #in case of exception this section will not execute
    print("Code is correct")
finally: #it will execute even if there is exception
    print("Code is correct__ ")