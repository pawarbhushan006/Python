# list are collection of data which can store any type of data, they ordered

student = ["Jhon", 20,80.5]
print(student)
print(type(student))

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_week[0])
# length of list == no of element sin list
print(len(days_of_week))

#slicing of list
print(days_of_week[1:6:2])

# concatenation
print(days_of_week + student)

#repetation
print(student *2)

#append() to add one iten at the end of list
fruits = ["apple", "banana", "orange"]

fruits.append("pear")
print(fruits)

print(fruits.append("apple")) #gives none as o/p becuase becasue append() dont return anything as it does not create new list

#insert()
#list.insert(index,item)
fruits.insert(1, "Dragon Fruit")

print(fruits)

'''extend() : can add many item at end of list in one go by providing list of value
remove()
pop()'''
fruits.extend(["apple", "banana", "orange"])
print(fruits)
fruits.append(["apple", "banana", "orange"])
print(fruits)

fruits.remove("banana")
fruits.remove("banana")
print(fruits)
fruits.pop(-2) #if we dont pass index by default last element will be poped
print(fruits)

'''revers()
sort() : by default it is in ascending order
count()
membership operation'''

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_week)
days_of_week.reverse()
print(days_of_week)

numbers = [1, 5,3, 2,4, 6, 7, 8, 9, 10]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)  #to make it descending order
print(numbers)

num = [1,1,2,3,4,5,6,6,6,0,0,0,10]
print(num.count(0))

#in and not in  : will give trur if item is present
print(0 in num)
print(7 not in num)

numbers=[10,4,5.5,7,1]
#smallest number in list
#min()
print(min(numbers))
print(f"biggest number:{max(numbers)}")
#numbers=[10,4,5.5,7,1,"hi"] in such case we cant use min max
#function it will throw typeerror as list is having mix typed data

print(sum(numbers))

#nested list
list1 = [5,1.5,'Python',True,[1,2,3],10]
print(list1[-2])
print(list1[-2][0])

