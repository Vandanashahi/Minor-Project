def check_id(id):
    if id.isdigit() and len(id) == 3:
        return True
    print("ID must be 3 digits")
    return False

def check_name(name):
    if name.replace(" ", "").isalpha():
        return True
    print("Name must contain letters only")
    return False

def check_address(address):
    if address.strip() != "":
        return True
    print("Address cannot be empty")
    return False

def check_contact(contact):
    if contact.isdigit() and len(contact) == 10 and contact[0] in "6789":
        return True
    print("Contact must be 10 digits starting with 6,7,8 or 9")
    return False