"""
 while loop: Used for indefinite iteration. This means the loop continues as long as a
certain condition remains True. You don't necessarily know the number of repetitions
when the loop starts; it keeps going until the condition becomes False.
"""
'''
while condition:
    statement
'''

num = 1
while num <= 2:
    print(num)
    num += 1

#infinite loop
correct_password = "Arrow@006"

# while True:
#     user_pwd = input("Enter Password: ")
#     if user_pwd == correct_password:
#         print("Correct Password")
#         break
#     else:
#         print("Incorrect Password, try again!")

num = 20

while num >= 10:
    print(num)
    num = num- 1

