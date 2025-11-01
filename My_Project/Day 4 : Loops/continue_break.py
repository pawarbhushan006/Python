for num in range(10):
    if num % 3 == 0 :
        continue   #gives control to start of the loop by skipping all statement which are written post continue
    print(num)

for num in range(1,10):
    if num % 3 == 0:
        break  # which makes control flow to go out of loop, basically it ends the loop
    print(num)
