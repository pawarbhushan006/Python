#positional argument: passing the arguments in order to their position
# def add(num1,num2):
#     res1 = num1 + num2
#     print(res1)
#
# add(1,2)
#
#
# #default argument: assign default argument to one or more argument
# def subtract(num1,num2=10):
#     res1 = num1 - num2
#     print(res1)
#
# subtract(10)
#
# #non default arguments should NOT follow the default argument
# def multiply(num1,num2=10,num3=1):
#     res1 = num1 + num2 + num3
#     print(res1)
# multiply(10,5)
#
# #keyword argument/named argument
# multiply(num1=10,num3=0)

#*args  -  variable length positional arguments 0 to n
#*args - stores data in tuples

def add(*args):
    print(sum(args))

add(1,2,3,4,5)

#**kwargs : variable length keyword arguments 0 to n
#kwargs stores data in dict
def func(**kwargs):
    print(kwargs)

func(x=10, y=20, z=30)

def student_details(sid, sname, **marks):
    if len(marks) == 0:
        print(f'Student {sname} has no marks')
    else:
        percentage = sum(marks.values()) / len(marks)
        print(f'Student {sname} has secured {percentage:.2f}%')

student_details(101,"Jhone", eng=80, math=99,bio=50)

