"""A program that will store the student ID numbers of 
a variable number of students specified by the program's user """


no_of_students = input("How many students will sit in the exam?: ")
while no_of_students.isnumeric() is False:
    print("Please enter a numerical value.")
    no_of_students = input("How many students will sit in the exam?: ")
no_of_students = int(no_of_students)

with open("reg_form.txt", "w", encoding = "utf-8") as students:
    for i in range(no_of_students):
        student_id = input("Enter the student's ID:")
        students.write(f"{student_id}\n")
        students.write("-" * 80)
        students.write("\n")
