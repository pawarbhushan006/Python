# for j in range(1,6):
#     print("* "*j)
from idlelib.autocomplete import FORCE

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

for i in range(6,1,-1):
    for j in range(1,i-1):
        print('*',end=" ")
    print()

m=max(range(1,6))
for i in range(1,6):
    for j in range(1, m+1):
        print(" " , end=" ")
    for k in range(1,i+1):
        print('*',end=" ")
    print()
    m-=1

m=max(range(1,6))
for i in range(1,6):
    for j in range(1, m+1):
        print(" " , end="")
    m -= 1
    for k in range(1,i+1):
        print('*',end=" ")
    print()
######################

print("Hollow Square Star Pattern")

for i in range(5): # 0,1,2,3,4
    for j in range(5): # 0,1,2,3,4
        if i == 0 or i == 5-1 or j == 0 or j == 5-1:  # this if condition check where to print * at first and last row
            #where i= 0 or side and j= 0 or side  it will print whole line and for other at end of side only
            #j is for rest row and i is for first and last row
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()

print("Filled Square Star Pattern")
for i in range(5):
    for j in range(5):
        print('*', end = ' ')

    print()



m=max(range(1,6))
for i in range(1,6):
    for j in range(1, m+1):
        print(" " , end=" ")
    for k in range(1,i+1):
        print('*',end=" ")
    print()
    m-=1
m=max(range(1,5))
for i in range(6,1,-1):
    for j in range(1,m+1):
        print(' ',end="")
    m -= 1
    for k in range(1,i-1):
        print('*',end=" ")
    print()

