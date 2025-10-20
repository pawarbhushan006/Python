countries = ["India", "USA", "Canada","Australia","Ireland", "Sri Lanka", "Spain","Cuba","Iran","Poland","Iceland"]

counter = 0
op =[]
for i in countries:
    if i.startswith('I'): #i[0] == 'I'
        counter +=1
        op.append(i)

print(counter)
print(op)
