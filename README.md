# Student Exam & Results Management System

## Overview

The **Student Exam & Results Management System** is a Python-based console application developed using **Object-Oriented Programming (OOP)** principles. The project was created as part of an Object-Oriented Programming assignment to demonstrate the practical application of classes, objects, methods, and Python data structures in solving a real-world problem in the **Education** domain.

The system enables users to register students, record examination results, calculate grades and GPA, generate performance remarks, update student information, and display student records through a simple menu-driven interface.

---

# Project Objectives

The objectives of this project are to:

- Register new students.
- Store student information using Object-Oriented Programming.
- Record examination results.
- Calculate grades automatically.
- Calculate GPA automatically.
- Generate performance remarks.
- Record the date when results are entered.
- Display student information.
- Search for students using their Student ID.
- Update a student's programme.
- Demonstrate the use of Object-Oriented Programming concepts.

---

# Features

- Student Registration
- Record Student Results
- Automatic Grade Calculation
- GPA Calculation
- Performance Remarks
- Date Recorded
- Display All Students
- Search Student by ID
- Update Student Programme
- Display Total Registered Students
- Input Validation for Examination Scores
- Menu-Driven Interface

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Dictionary Data Structure
- Tuple
- Git

---

# Object-Oriented Programming Concepts Demonstrated

This project demonstrates the following OOP concepts:

- Classes
- Objects
- Attributes
- Instance Methods
- Class Methods (`@classmethod`)
- Static Methods (`@staticmethod`)
- Object Interaction
- Encapsulation
- Modularity

---

# Python Data Structures Used

## Dictionary

A dictionary is used to store Student objects using the Student ID as the unique key.

Example:

```python
students = {
    "ST001": student1,
    "ST002": student2
}
```

## Tuple

The project also uses a tuple to store fixed grade values.

```python
GRADE_LEVELS = ("A", "B", "C", "D", "F")
```

---

# Project Structure

```text
StudentExamResultsSystem/
│
├── student_exam_results_system.py
├── README.md
└── screenshots
```

---

# How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project in PyCharm, Visual Studio Code, or IDLE.
4. Run:

```bash
python student_exam_results_system.py
```

5. Follow the on-screen menu.

---

# Sample Menu

```text
==========================================
 STUDENT EXAM & RESULTS MANAGEMENT SYSTEM
==========================================

1. Register Student
2. Record Student Result
3. Display All Students
4. Search Student
5. Display Student Result
6. Update Programme
7. Total Registered Students
8. Exit
```

---

# Example Output

```text
------ Student Information ------

Student ID : ST001
Name       : John Adel Sesay
Programme  : Software Engineering
Level      : Year One

------ Student Result ------

Subject        : Python Programming
Score          : 85
Grade          : A
GPA            : 4.0
Remark         : Excellent
Date Recorded  : 27-10-2026
```

---

# Digital Public Goods (DPG) Alignment

This project follows the Digital Public Goods (DPG) principles.

### Open Source

The source code is intended to be publicly available on GitHub so that others can learn from, reuse, and improve the project.

### Inclusive and Accessible

The application uses a simple, menu-driven interface with clear prompts, making it easy to use for people with basic computer skills.

### Privacy Respecting

The system stores only the information required for educational purposes:

- Student ID
- Student Name
- Programme
- Level
- Subject
- Examination Score

No unnecessary sensitive personal information is collected or stored.

### Modular and Reusable

The program is divided into reusable classes and functions, making it easy to maintain and extend with additional features in the future.

---

# Future Improvements

Possible future enhancements include:

- Database integration (MySQL or SQLite)
- User authentication
- Multiple subjects per student
- Semester management
- GPA based on multiple courses
- Student transcript generation
- Report printing (PDF)
- Graphical User Interface (GUI)
- Web-based version

---

# Author

**John Adel Sesay**

Software Engineering Student

---

# License

This project is released for educational purposes. It may be used, studied, modified, and shared with appropriate acknowledgement.

---

# Acknowledgements

This project was developed as part of an Object-Oriented Programming course assignment to demonstrate the practical application of Python and Object-Oriented Programming concepts in solving a real-world problem within the Education domain.