#sets also collection of item but sets are non sequential collection and it cannot be indexed
#sets{}

s1= {10, "Python",(1,2)}
# we cant have list as element of set
print(s1)
print(len(s1))
#indexing slicing not allowed

#sets dont allow duplicate element, even if enter
# duplicate value it will store only single instance of that element
s1={1,2,3,4,5,1}
print(s1)

#membership operator: in and not in
print(1 in s1)
print(10 not in s1)

#concate
num1={1,2,3}
num2={2,3}
#num31=num1+num2  this is not supported
#num1*3 this is also not supported in sets
#type casting is possible from sets to list or tuples and vice versa

#operation
#add()
num1.add(5) #add function does not return any value
print(num1)
#remove
num1.remove(3)
print(num1)
#discard
num1.discard(4) #it will not give error even if element which we want to delet is not available in set,
#but remove will throw error in such scenario
num1={1,2,3}
num2={2,3,5}
#unions,intersection, difference
print(num1.union(num2)   )
#for uninon we can use below syntax
s3= num1|num2
print(s3)
print(num1.intersection(num2) )
#for this we can use &
num3= num1&num2
print(num3)
print("diff")
print(num1.symmetric_difference(num2) )
print(num2.symmetric_difference(num1) )
print("^")
print(num1 ^ num2)
print(num1.difference(num2) )
print(num2.symmetric_difference(num1))
num3=num1-num2
print(num3)

#frozen sets are immutable

s1={1,2,5,0}
fs1 = frozenset(s1)
print(fs1)
fs1=frozenset({10,20,30})
print(fs1)
fs2=frozenset((10,20,30))
print(fs2)

print(fs1 | fs2)
print(fs1 & fs2)
print(fs1 ^fs2)
