# ============================================
# STUDENT EXAM & RESULTS MANAGEMENT SYSTEM
# Object-Oriented Programming (OOP) Assignment
# Domain: Education
# ============================================

from datetime import datetime

GRADE_LEVELS = ("A", "B", "C", "D", "F")


class Student:
    total_students = 0

    def __init__(self, student_id, name, programme, level):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.level = level
        self.result = None
        Student.total_students += 1

    def display_info(self):
        print("\n------ Student Information ------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Programme  : {self.programme}")
        print(f"Level      : {self.level}")

    def update_programme(self, new_programme):
        self.programme = new_programme
        print("Programme updated successfully.")

    @classmethod
    def get_total_students(cls):
        print(f"\nTotal Registered Students: {cls.total_students}")

    @staticmethod
    def validate_score(score):
        return 0 <= score <= 100


class Result:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score
        self.date_recorded = datetime.now().strftime("%d-%m-%Y")

    def calculate_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        return "F"

    def calculate_gpa(self):
        if self.score >= 70:
            return 4.0
        elif self.score >= 60:
            return 3.0
        elif self.score >= 50:
            return 2.0
        elif self.score >= 40:
            return 1.0
        return 0.0

    def get_remark(self):
        if self.score >= 70:
            return "Excellent"
        elif self.score >= 60:
            return "Very Good"
        elif self.score >= 50:
            return "Good"
        elif self.score >= 40:
            return "Pass"
        return "Fail"

    def display_result(self):
        print("\n------ Student Result ------")
        print(f"Subject        : {self.subject}")
        print(f"Score          : {self.score}")
        print(f"Grade          : {self.calculate_grade()}")
        print(f"GPA            : {self.calculate_gpa()}")
        print(f"Remark         : {self.get_remark()}")
        print(f"Date Recorded  : {self.date_recorded}")


students = {}


def register_student():
    print("\n===== Register Student =====")
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists.")
        return
    name = input("Enter Student Name: ")
    programme = input("Enter Programme: ")
    level = input("Enter Level: ")
    students[student_id] = Student(student_id, name, programme, level)
    print("Student registered successfully.")


def record_result():
    print("\n===== Record Student Result =====")
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    subject = input("Enter Subject: ")
    while True:
        try:
            score = float(input("Enter Score (0-100): "))
            if Student.validate_score(score):
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    students[student_id].result = Result(subject, score)
    print("Result recorded successfully.")


def display_students():
    if not students:
        print("\nNo students registered.")
        return
    print("\n===== Student List =====")
    for student in students.values():
        student.display_info()


def search_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        students[student_id].display_info()
    else:
        print("Student not found.")


def display_student_result():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    student = students[student_id]
    student.display_info()
    if student.result:
        student.result.display_result()
    else:
        print("No result recorded for this student.")


def update_programme():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    new_programme = input("Enter New Programme: ")
    students[student_id].update_programme(new_programme)


def main():
    while True:
        print("\n==========================================")
        print(" STUDENT EXAM & RESULTS MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Register Student")
        print("2. Record Student Result")
        print("3. Display All Students")
        print("4. Search Student")
        print("5. Display Student Result")
        print("6. Update Programme")
        print("7. Total Registered Students")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            record_result()
        elif choice == "3":
            display_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            display_student_result()
        elif choice == "6":
            update_programme()
        elif choice == "7":
            Student.get_total_students()
        elif choice == "8":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
