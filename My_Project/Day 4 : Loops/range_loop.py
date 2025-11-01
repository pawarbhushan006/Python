#range()- it used to generate sequence of integers
#range(startint, stopint, step), by default step is 1
#range(5) : 5 is stop range
'''
for i in range(start, end, step)
    statement
'''

for i in range(1,10,2 ): #in range function end int will not be generated
    print(i)

#to generate in reverse oreder
for i in range(11,0,-1):
    print(i)

profits = [1,9,10,5]
for i in range(len(profits)):
    print(profits[i])