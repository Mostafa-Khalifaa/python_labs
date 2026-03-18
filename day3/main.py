from students import *
from grades import *

students_file()
grades_file()

print("-----------------------------------------")

show_students()

print("-----------------------------------------")

show_grades()

print("-------------------------------------")

student_id = input("Enter ID: ")
name = find_student(student_id)

if name == "":
    print("Student not found")
else:
    print("Student Name:", name)
    student_grades(student_id)

print("-----------------------------------------")
average()
