import pickle

class Course_Grades:

    def __init__(self, course_name, stu_ID, stu_grade):
        self.course_name = course_name
        self.stu_ID = stu_ID
        self.stu_grade = stu_grade

    def display(self):
        print("Course Name:", self.course_name)
        print("Student ID:", self.stu_ID)
        print("Student Grades:", self.stu_grade)

course1_name = input("Enter the course name for Course 1:")
course1_stu_ID = int(input("Enter student ID:"))
course1_stu_grade = int(input("Enter Grade:"))

course2_name = input("Enter the course name for Course 2:")
course2_stu_ID = int(input("Enter student ID:"))
course2_stu_grade = int(input("Enter Grade:"))

course3_name = input("Enter the course name for Course 3:")
course3_stu_ID = int(input("Enter student ID:"))
course3_stu_grade = int(input("Enter Grade:"))

course4_name = input("Enter the course name for Course 4:")
course4_stu_ID = int(input("Enter student ID:"))
course4_stu_grade = int(input("Enter Grade:"))

course1 = Course_Grades(course1_name, course1_stu_ID, course1_stu_grade)
course2 = Course_Grades(course2_name, course2_stu_ID, course2_stu_grade)
course3 = Course_Grades(course3_name, course3_stu_ID,course3_stu_grade)
course4 = Course_Grades(course4_name, course4_stu_ID,course4_stu_grade)

with open("grades_info.dat", "ab") as file:
    pickle.dump(course1, file)
    pickle.dump(course2, file)
    pickle.dump(course3, file)
    pickle.dump(course4, file)

with open("grades_info.dat", "rb") as f:
    while True:
        try:
            course = pickle.load(f)
            course.display()
        except EOFError:
            break