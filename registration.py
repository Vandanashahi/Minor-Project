from validation import check_id, check_name, check_address, check_contact

def register(students):
    print("\n--- Register New Student ---")
    while True:
        id = input("ID (3 digits): ").strip()
        if check_id(id) and id not in [s["id"] for s in students]:
            break
        print("Invalid or already used ID!")

    name = input("Name: ").strip()
    while not check_name(name):
        name = input("Name again: ").strip()

    address = input("Address: ").strip()
    while not check_address(address):
        address = input("Address again: ").strip()

    contact = input("Contact: ").strip()
    while not check_contact(contact):
        contact = input("Contact again: ").strip()

    students.append({"id": id, "name": name, "address": address, "contact": contact})
    print("Registered successfully!\n")

def view_all(students):
    print("\n--- All Students ---")
    if not students:
        print("No students yet!\n")
        return
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['address']} | {s['contact']}")
    print()

def search_by_id(students):
    print("\n--- Search by ID ---")
    id = input("Enter ID: ").strip()
    for s in students:
        if s["id"] == id:
            print("Found:")
            print(f"   ID      : {s['id']}")
            print(f"   Name    : {s['name']}")
            print(f"   Address : {s['address']}")
            print(f"   Contact : {s['contact']}\n")
            return
    print("Not found!\n")

def update_student(students):
    print("\n--- Update Student ---")
    id = input("Enter ID: ").strip()
    for s in students:
        if s["id"] == id:
            print("Current:", s)
            name = input("New name (blank = keep): ").strip()
            address = input("New address (blank = keep): ").strip()
            contact = input("New contact (blank = keep): ").strip()

            if name: s["name"] = name
            if address: s["address"] = address
            if contact and check_contact(contact):
                s["contact"] = contact
            elif contact:
                print("Invalid contact – not changed")

            print("Updated!\n")
            return
    print("Student not found!\n")

def delete_student(students):
    print("\n--- Delete Student ---")
    id = input("Enter ID: ").strip()
    for i in range(len(students)):
        if students[i]["id"] == id:
            print("Deleting:", students[i])
            if input("Sure? (y/n): ").lower() == "y":
                students.pop(i)
                print("Deleted!\n")
            else:
                print("Cancelled")
            return
    print("Not found!\n")