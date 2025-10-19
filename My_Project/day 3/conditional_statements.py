marks = float(input("Enter marks: "))
if marks <= 18:
    print("You are fail.")
elif marks >= 70:
    print("You are success.")
elif marks >= 60:
    print("You are success bit on vegrge.")
else:
    print("no record ")
print("we are out of if")

#ternary operator

num=int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# trueexpressiion if condition else false expression
print(num,"is even") if num % 2 == 0 else print(num, "is odd")