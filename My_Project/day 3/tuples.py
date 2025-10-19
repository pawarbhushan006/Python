#tuple: (item, item2,...)
# sequence of item as a collection
# modification of tuple is not possible

t1= ('python',10, 1.5, True,None,[1,2,3],(1,2,3))
print(t1)
print(len(t1))

#access
print(t1[0])
print(t1[-1][0])
print(t1[1:4:2])


#paranthesis are not necessary to create tuples
t2 = 10,20,30,40
print(type(t2))
#type casting from tuple to list and vice versa is possible
#operations on tuples
#concatenation
sd1 = (1001,"Jhon")
sd2 =(100,20,45,75.5)

sd = sd1+sd2
print(sd)
#repetation
t1=("Class 5", 5000)
print(t1*3)

#in not in
print(100 in sd)
print(99 not in sd)

#count
print(sd.count("Python"))
print(sd.count("Jhon"))
#print(sd.index("Python")) this will not work an dit will throw an error as element is not there in tuple
print(sd.index(100))

t1=10, 20,3,4,5,3,5,6
print(t1.index(3))
#index function always gives index for first occurrence of value /element
#min,max and sum function can be used in case of tuples
