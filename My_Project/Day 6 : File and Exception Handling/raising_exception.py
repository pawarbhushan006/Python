from sys import exception

salary = float(input("Enter the salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative")
    #raise exception(salary) #this also can be used to raise exception
else:
    print(f"Salary is valid {salary}")

