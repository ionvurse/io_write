"""A program that will crate a text file and write the student IDs of 
a variable number of students specified by the program's user.
Dotted lines added between each IDs so that the text file could be 
printed as an attendance register"""

no_of_students = input("How many students will sit in the exam?: ")

"""The while loop will continue to ask for a numerical value,
if the input is of a different data type"""
while no_of_students.isnumeric() is False:
    print("Please enter a numerical value.")
    no_of_students = input("How many students will sit in the exam?: ")

# Casting the number entered into an integer
no_of_students = int(no_of_students)

# creating an empty list that will store the Student's IDs
students_register = []
for i in range(no_of_students):
    student_id = input("Enter a student's ID:")
    students_register.append(student_id + "\n")
    students_register.append("-" * 80 + "\n")

# use write() and writelines() methods to format the text file for printing
with open("reg_form.txt", "w", encoding = "utf-8") as students:
    students.write("Student ID" + "\t" * 12 + "Signature\n")
    students.write("-" * 80 + "\n")
    students.writelines(students_register)