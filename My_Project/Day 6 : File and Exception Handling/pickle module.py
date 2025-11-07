import pickle

students = {'Studnet1':{'roll':101, 'name':'Jhon','percent':78.5},
            'Student1':{'roll':102, 'name':'Carol','percent':98.5},
            'Student3':{'roll':103, 'name':'Elly','percent':87.5} }

#print(students)

# with open("students.txt","wt") as file:
#     file.write(str(students))

# with open("students.txt","rt") as file:
#     for student in file:
#         print(student)


#pickle module is used in python to store the content and access it back in required format

#serialization|

with open("students.bin","bw") as file:
    for i in students:
        pickle.dump(students[i],file)

#de-serialization : since we loaded file one by one while reading we can read it row by row, for example her eto read 3 rows we need to use print 3 times
with open("students.bin","rb") as file:
    while True:
        try:
            student = pickle.load(file)
            print(student)
        except EOFError:
            print('Done!')
            break

#print student name who scored more than 90%
student_list_90=[]
with open("students.bin","rb") as file:
    while True:
        try:
            student = pickle.load(file)
            if student['percent'] >=90 :
                student_list_90.append(student['name'])
        except EOFError:
            break

print(student_list_90)

