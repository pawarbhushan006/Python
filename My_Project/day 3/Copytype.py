#shallow_deep_copy
import copy

l1= [1,2.5,[10,20,30],'Python']

#shallow Copy : it will have have diff memory loc for copied object
l2= copy.copy(l1)
print(id(l1))
print(id(l2))

l1[0]=5
l2[2][0] = 50
print(f"l1-> {l1}",id(l1))
print(f"l2-> {l2}",id(l2))
'''
o/p
l1-> [5, 2.5, [50, 20, 30], 'Python'] 4367076480
l2-> [1, 2.5, [50, 20, 30], 'Python'] 4367651264
#: notice here l1 first element update and list first element also
even though there is no direct operation , but internal element is getting updated as it is haing same memory location 
when we are doing shallow copy|

basically both list will share same address
'''
#deep copy

l1= [1,2.5,[10,20,30],'Python']

#shallow Copy : it will have have diff memory loc for copied object
l2= copy.deepcopy(l1)
print(id(l1))
print(id(l2))

l1[0]=5
l2[2][0] = 50
print(f"l1-> {l1}",id(l1))
print(f"l2-> {l2}",id(l2))

'''
l1-> [5, 2.5, [10, 20, 30], 'Python'] 4379227712
l2-> [1, 2.5, [50, 20, 30], 'Python'] 4367076480

it is allocating diff memory location for internal element also 

here 
'''






