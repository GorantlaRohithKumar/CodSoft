# Contact Book Dictionary
contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(query):
    found_contacts = []
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            found_contacts.append(contact)
    
    if found_contacts:
        print("Search results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    query = input("Enter the name or phone number to update: ")
    for contact in contacts:
        if query == contact['name'] or query == contact['phone']:
            print("Contact found. Enter new details:")
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            
            contact['name'] = name
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")

def delete_contact():
    query = input("Enter the name or phone number to delete: ")
    for contact in contacts:
        if query == contact['name'] or query == contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")

# Main menu
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        query = input("Enter the name or phone number to search: ")
        search_contact(query)
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")
