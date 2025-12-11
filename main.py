import json
import os

from registration import register, view_all, search_by_id, update_student, delete_student

FILE = "student.json"
students = []       

def load_data():
    global students
    if os.path.exists(FILE):
        with open(FILE) as f:
            students = json.load(f)
        print(f"Loaded {len(students)} student(s).\n")
    else:
        students = []
        print("No saved data. Starting fresh!\n")

def save_data():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def main():
    load_data()

    while True:
        print("\n=== Student Management System ===")
        print("1. Register Student")
        print("2. View / Search Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("\nChoose (1-5): "))
        except:
            print("Enter a number only!\n")
            continue

        if choice == 1:
            register(students)
            save_data()
        elif choice == 2:
            while True:
                print("\n--- View or Search ---")
                print("1. View All Students")
                print("2. Search by ID")
                print("3. Back")
                while True:
                    try:
                        sub = int(input("\nChoose (1-3): "))
                        if sub in [1, 2, 3]:
                            break
                        else:
                            print("Please enter 1, 2 or 3 only!")
                    except ValueError:
                        print("Invalid! Enter number only!")

                if sub == 1:
                    view_all(students)
                elif sub == 2:
                    search_by_id(students)
                elif sub == 3:
                    break
        elif choice == 3:
            update_student(students)
        elif choice == 4:
            delete_student(students)
            save_data()
        elif choice == 5:
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice!\n")

main()