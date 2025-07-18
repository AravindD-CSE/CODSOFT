contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("All Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        print("Contact updated!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("Contact Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose options: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you")
            break
        else:
            print("Invalid option.\n")

menu()
