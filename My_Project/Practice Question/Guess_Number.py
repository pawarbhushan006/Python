import random

random_num = random.randint(1,100)
#print(random_num)
counter =10
for i in range(11):
    print(f'You have {counter} attempts left')
    a = int(input("Enter your guess between 1-100:"))

    if a == random_num:
        print("Correct")
        break
    elif a>random_num:
        print("enter lower value")
    elif a<random_num:
        print("enter higher value")
    else:
        print("wrong guess")
    counter -= 1

