import json
students = {'Student1':{'roll':101, 'name':'Jhon','percent':88.5,'sports':True},
            'Student2':{'roll':102, 'name':'Carol','percent':98.5, 'sports':True},
            'Student3':{'roll':103, 'name':'Elly','percent':87.5,'sports':False} }

# with open("students.json","w") as file:
#     json.dump(students,file,indent=4)
#
# with open("students.json","r") as file:
#     students = json.load(file)
#     print(students)

#update()
#1st step : read old data first
try:
    with open("students.json","r") as file:
        students_up = json.load(file)
except FileNotFoundError:
    with open("students.json","w") as file:
        json.dump(students,file)
else:
    students_up.update(students)
    with open("students.json","w") as file:
        json.dump(students_up,file,indent=4)