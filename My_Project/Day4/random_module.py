#modules: python files that has code return it, we can create our own modules which can be used in your code
#python has there own standard modules which we can use , which needs to import

import random

#random(): returns any random number between 0.0 and 1.0 where 1.0 is excluded

print(random.random())

#randint(a,b) : take two parameter to define range and it generated random integer
print(random.randint(1,10))

nums= ["one","two","three","four","five"]
#choice(sequence) : returns a random item from the sequence
print(random.choice(nums))
print(nums)
#shuffle() => returns the elements shuffled in random order, this changes order permanently
random.shuffle(nums)
print(nums)
