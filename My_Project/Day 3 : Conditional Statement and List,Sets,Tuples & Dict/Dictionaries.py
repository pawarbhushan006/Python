#dic{key1:val1, ....}

groceries ={'milk':60,
          'bread':100, 'rice':90, 'test':(1,2,3)}
#keys can be integer,float,boolean,tuple or strings only not set dict or list: the reason is this are mutable

print(groceries)

#len
print(len(groceries))

#indexing not possible in dict
print(groceries['milk'])
#get()
print(groceries.get('water')) #it will give value if the key exist in dict but if does not exist then it will give none
print(groceries['bread']) #for non existing key it will throw error

#get can help to return default value for non existing key for existing key it will return actual value
print(groceries.get('water',10000))

groceries['milk']=1000 #updates the value for the respective key
print(groceries)
groceries['eggs']=100 #this add directly new element to dict
print(groceries)

#membership in dic - in and not in : it work on key not on value
print(1000 in groceries)
print('milk' in groceries)

sem1_marks ={'maths':100,
              'chemistry':100, 'Physics':100}
sem2_marks ={'English':100,'Biology':100}
print(sem1_marks.update(sem2_marks))
#in case we have same key in both dict then value with pass dict as parameter dicy key will be replaced

print(sem1_marks.pop('Biology'))

groceries ={'milk':60,
          'bread':100, 'rice':90, 'milk':70}
print(groceries)

#in case we pass duplicate key, python will show warning not an error and it will consider last value assigned to the key
#in above case milk will have 70 as value instead on 60  as it reads from left to right in case of dict and o/p will like below
#{'milk': 70, 'bread': 100, 'rice': 90}

#function: keys(),values(),items()
print(groceries.keys())
print(groceries.values())
print(groceries.items(),type(groceries.items())) #to get key value pair , and it stored as tuple
# dict_items([('milk', 70), ('bread', 100), ('rice', 90)])


