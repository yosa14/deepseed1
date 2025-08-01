student_gradebook = {}

def add_student():
    name = input("Enter student name: ").strip()
    if name in student_gradebook:
        print("Student already exists.")
    else:
        student_gradebook[name] = []
        print(f"{name} added.")

def add_grade():
    name = input("Enter student name to add grade to: ").strip()
    if name in student_gradebook:
        try:
            grade = float(input("Enter student grade: "))
            student_gradebook[name].append(grade)
            print("Grade added.")
        except ValueError:
            print("Invalid grade.")
    else:
        print("Student not found.")

def view_report():
    name = input("Enter student name: ").strip()
    if name in student_gradebook:
        grades = student_gradebook[name]
        if grades:
            avg = sum(grades) / len(grades)
            if avg >= 90:
                letter = "A"
            elif avg >= 80:
                letter = "B"
            elif avg >= 70:
                letter = "C"
            elif avg >= 60:
                letter = "D"
            else:
                letter = "F"

        print(f"{name}'s Average: {avg:.2f} (Grade: {letter})")
        print("Grades:", grades)
    else:
            print("No grades yet."),


def class_stats():
    if not student_gradebook:
        print("No students yet.")
        return

    total = 0
    count = 0
    top_student = None
    top_avg = 0
    low_student = None
    low_avg = 100

    for name, grades in student_gradebook.items():
        if grades:
            avg = sum(grades) / len(grades)
            total += avg
            count += 1
            if avg > top_avg:
                top_avg = avg
                top_student = name
            if avg < low_avg:
                low_avg = avg
                low_student = name

    if count:
        class_avg = total / count
        print(f"Class Average: {class_avg:.2f}")
        print(f"Top Student: {top_student} ({top_avg:.2f})")
        print(f"Lowest Student: {low_student} ({low_avg:.2f})")
    else:
        print("No grades yet.")

while True:
    print("\n=== STUDENT GRADEBOOK MANAGER ===")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student Report")
    print("4. Class Statistics")
    print("5. Exit")

    choice = input("Choice: ").strip()


    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        view_report()
    elif choice == "4":
        class_stats()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")



    
