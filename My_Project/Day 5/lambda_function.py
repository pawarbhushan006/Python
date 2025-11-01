#annonymus function or lambada function
'''
 lambda functions provide a convenient and concise way to define small, single-expression functions in Python,
 particularly useful when an anonymous function is needed as an argument to another function or for quick,
 inline operations.
'''
#syntax: lambada argument: expression

fun=  lambda num1, num2:  num1+num2
res =fun(2,5)
print (res)

#filter and map function where lambada function can be used

#filter :  here fuction is first argument and sequence is second argument
#filter(function(), sequence)
#Constructs an iterator from elements of an iterable for which a function returns true.

seq = [1,2,3,4,5]

odd = lambda x:True if x%2==0 else False
odd2 = lambda x: x%2==0
output = filter(odd,seq)

print(list(filter(odd2,seq)))

print(output) # when try to call filter function it returns filter object or memort location,
# we can either use loop of list() function to get actual value
print(list(output))

#map() : Applies a function to each item in an iterable.

square = lambda num: num*num
print (list(map(square,seq)))

seq = [1,2,3,4,5]

odd = lambda x:True if x%2==0 else False
odd2 = lambda x: x%2==0
output = map(odd,seq)

print(list(map(odd2,seq)))
print(list(output))




