"""A program that will store the student ID numbers of 
a variable number of students specified by the program's user """

# if no_of_students.isnumeric() is False:
#     # print("How many students will sit in the exam?: ")
#     no_of_students = input("""\tHow many students will sit in the exam?:
#         Please enter a numeric value: """)
# else:
#     no_of_students = int(no_of_students)
#     print(no_of_students)
no_of_students = input("\tHow many students will sit in the exam?: ")
no_of_students = int(no_of_students)

with open("reg_form.txt", "w", encoding = "utf-8") as students:
    for i in range(no_of_students):
        student_id = input("Enter the student's ID:")
        student_id = int(student_id)
        students.write(f"{student_id}\n")
        students.write("-" * 60)
        students.write("\n")
