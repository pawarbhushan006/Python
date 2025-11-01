#module is file containing definitions and statements
#any file with .py extension in file name is module
#math, random, datetime etc are example

import math
from random import randint
# we can import specific function or variable from module : form module_name import f1, f2,f3 ...

#square roor of num
num =100
print(math.sqrt(num))

#area of circle
r= 5
print(f"Area of circle{math.pi*r**2:.2f}")

#val = random.randint(1,100) # this will not work as we have imported only specific function randit ()
val = randint(1,100)
print(val)

# we can alias imported module name : import module name as alias_name

