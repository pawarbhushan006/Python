import random

print("welcome to dice game")



while True:
    choice = input("enter your choice:Press Enter to roll dice and q to quit")

    if choice == "q":
        print("thank you for playing")
        break
    elif choice == "":
        random_dice=random.randint(1,6)
        print(f'Dice has thrown and value is :{random_dice}')
    else:
        print("wrong choice")
