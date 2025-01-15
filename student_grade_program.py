# student_grade_program.py

# Step 1: Create a dictionary with student names and grades
student_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# Step 2: Print all students and their grades
print("Student Grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Step 3: Calculate the average grade
average_grade = sum(student_grades.values()) / len(student_grades)
print("\nAverage Grade:", average_grade)

# Step 4: Find the top student
top_student = max(student_grades, key=student_grades.get)
print("\nTop Student:")
print(f"{top_student}: {student_grades[top_student]}")

# Step 5: Add a new student
student_grades["Eve"] = 90
print("\nAfter Adding a New Student:")
print(student_grades)

# Step 6: Modify a student's grade
student_grades["Bob"] = 82
print("\nAfter Updating Bob's Grade:")
print(student_grades)

# Step 7: Remove a student
del student_grades["Alice"]
print("\nAfter Removing Alice:")
print(student_grades)