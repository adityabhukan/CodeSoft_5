import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully!")
    
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found in the list.")
            return
        
        print("\nContact List:")
        print("-" * 50)
        print(f"{'No.':<5}{'Name':<20}{'Phone':<15}{'Email':<30}{'Address':<30}")
        print("-" * 50)
        
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index:<5}{contact.name:<20}{contact.phone:<15}{contact.email:<30}{contact.address:<30}")
    
    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                found_contacts.append(contact)
        
        if not found_contacts:
            print("\nNo matching contacts found.")
            return
        
        print("\nSearch Results:")
        print("-" * 50)
        print(f"{'No.':<5}{'Name':<20}{'Phone':<15}{'Email':<30}{'Address':<30}")
        print("-" * 50)
        
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index:<5}{contact.name:<20}{contact.phone:<15}{contact.email:<30}{contact.address:<30}")
    
    def update_contact(self, contact_index):
        if contact_index < 0 or contact_index >= len(self.contacts):
            print("\nInvalid contact number.")
            return
        
        contact = self.contacts[contact_index]
        print(f"\nUpdating contact: {contact.name}")
        
        while True:
            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            print("4. Address")
            print("5. Finish Updating")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                contact.name = input("Enter new name: ").strip()
            elif choice == '2':
                contact.phone = self.get_valid_phone()
            elif choice == '3':
                contact.email = self.get_valid_email()
            elif choice == '4':
                contact.address = input("Enter new address: ").strip()
            elif choice == '5':
                print("\nContact updated successfully!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def delete_contact(self, contact_index):
        if contact_index < 0 or contact_index >= len(self.contacts):
            print("\nInvalid contact number.")
            return
        
        deleted_contact = self.contacts.pop(contact_index)
        print(f"\nContact '{deleted_contact.name}' deleted successfully!")
    
    def get_valid_phone(self):
        while True:
            phone = input("Enter phone number: ").strip()
            if re.match(r'^[0-9+\- ]+$', phone):
                return phone
            print("Invalid phone number. Please enter only numbers, +, or -.")
    
    def get_valid_email(self):
        while True:
            email = input("Enter email: ").strip()
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return email
            print("Invalid email format. Please enter a valid email.")

def display_menu():
    print("\nContact Management System")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            print("\nAdd New Contact")
            name = input("Enter name: ").strip()
            phone = manager.get_valid_phone()
            email = manager.get_valid_email()
            address = input("Enter address: ").strip()
            
            new_contact = Contact(name, phone, email, address)
            manager.add_contact(new_contact)
        
        elif choice == '2':
            manager.view_contacts()
        
        elif choice == '3':
            search_term = input("\nEnter name or phone number to search: ").strip()
            manager.search_contact(search_term)
        
        elif choice == '4':
            manager.view_contacts()
            if manager.contacts:
                try:
                    contact_num = int(input("\nEnter the contact number to update: ")) - 1
                    manager.update_contact(contact_num)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        elif choice == '5':
            manager.view_contacts()
            if manager.contacts:
                try:
                    contact_num = int(input("\nEnter the contact number to delete: ")) - 1
                    manager.delete_contact(contact_num)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        elif choice == '6':
            print("\nThank you for using the Contact Management System. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
