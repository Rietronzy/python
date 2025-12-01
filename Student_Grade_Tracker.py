# student_grade_tracker.py

grades = {}

def add_grade():
    student = input(" enter name: ")
    subject = input("Enter subject: ")
    grade = float(input("Enter grade: "))
    if student not in grades:
        grades[student] = {}
    grades[student][subject] = grade
    print("Grade added.")

def view_grades():
    student = input("Enter student name: ")
    if student in grades:
        print(f"Grades for {student}:")
        for subject, grade in grades[student].items():
            print(f"(ENGLISH):")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n1. Add grade")
        print("2. View grades")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()