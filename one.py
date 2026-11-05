# ==========================================
# Student Record Management System
# Developed in Python 3 using Dictionaries, Tuples, and Lists
# ==========================================

# Dictionary to store records: key = roll number, value = (name, course, marks)
student_records = {}


def add_record(roll_no, name, course, marks):
    """Create / Add operation: Ensures unique roll number and valid marks (0-100)."""
    try:
        roll_no = int(roll_no)
        marks = int(marks)
    except ValueError:
        print("Invalid input format for roll number or marks.")
        return

    # Check for unique roll number
    if roll_no in student_records:
        print(f"Roll number {roll_no} already exists.")
        return

    # Check for valid marks between 0 and 100
    if not (0 <= marks <= 100):
        print("Marks must be between 0 and 100.")
        return

    # Store record using a tuple inside the dictionary
    student_records[roll_no] = (name.strip(), course.strip(), marks)
    print(
        f"Record added: {roll_no} | {name.strip()} | {course.strip()} | {marks}"
    )


def view_records():
    """Read / View operation: Displays all student records in a neat table format."""
    if not student_records:
        print("No student records found.")
        return

    print("\n" + "-" * 50)
    print(f"{'Roll No':<10} | {'Name':<15} | {'Course':<10} | {'Marks':<5}")
    print("-" * 50)
    for roll_no, details in student_records.items():
        print(
            f"{roll_no:<10} | {details[0]:<15} | {details[1]:<10} |"
            f" {details[2]:<5}"
        )
    print("-" * 50)


def search_record(roll_no):
    """Read / Search operation: Finds and displays a record by roll number."""
    try:
        roll_no = int(roll_no)
    except ValueError:
        print(f"Roll number {roll_no} not found.")
        return

    if roll_no in student_records:
        details = student_records[roll_no]
        print(f"{roll_no} | {details[0]} | {details[1]} | {details[2]}")
    else:
        print(f"Roll number {roll_no} not found.")


def update_record(roll_no, new_marks):
    """Update operation: Updates the marks of an existing student record."""
    try:
        roll_no = int(roll_no)
        new_marks = int(new_marks)
    except ValueError:
        print("Invalid input format.")
        return

    if roll_no not in student_records:
        print(f"Roll number {roll_no} not found.")
        return

    if not (0 <= new_marks <= 100):
        print("Marks must be between 0 and 100.")
        return

    name, course, _ = student_records[roll_no]
    student_records[roll_no] = (name, course, new_marks)
    print(f"Marks updated: {new_marks}")


def delete_record(roll_no):
    """Delete operation: Removes a student record by roll number."""
    try:
        roll_no = int(roll_no)
    except ValueError:
        print(f"Roll number {roll_no} not found.")
        return

    if roll_no in student_records:
        del student_records[roll_no]
        print(f"Record deleted: {roll_no}")
    else:
        print(f"Roll number {roll_no} not found.")


def main():
    """Console menu interface to execute CRUD operations."""
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            marks = input("Enter Marks: ")
            add_record(roll_no, name, course, marks)
        elif choice == "2":
            view_records()
        elif choice == "3":
            roll_no = input("Enter Roll Number to Search: ")
            search_record(roll_no)
        elif choice == "4":
            roll_no = input("Enter Roll Number to Update: ")
            new_marks = input("Enter New Marks: ")
            update_record(roll_no, new_marks)
        elif choice == "5":
            roll_no = input("Enter Roll Number to Delete: ")
            delete_record(roll_no)
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
