# 1. Create a dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 68,
    "Eve": 77
}

# 2. Ask the user to input a student's name
student_name = input("Enter a student's name to see their marks: ")

# 3. Retrieve and display the corresponding marks
# 4. If the student’s name is not found, display an appropriate message
if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name}'s marks are: {marks}")
else:
    print("Student name not found")

