import re
import os

# Example names to test
example_names = [
    "John Doe",
    "Jane",
    "Alice Smith",
    "Bob",
    "Charlie Brown",
    "David",
    "Eve Adams",
    "Frank",
    "Grace Hopper",
    "Henry"
]

# Example emails to test
example_emails = [
    "john.doe@example.com",
    "jane_doe123@example.co.uk",
    "alice.smith@example.org",
    "bob@example.net",
    "charlie.brown@example.com",
    "david@example.com",
    "eve.adams@example.io",
    "frank@example.edu",
    "grace.hopper@example.com",
    "henry@example.com",
    "user+mailbox/department=shipping@example.com",
    "customer/department=shipping@example.com",
    "$A12345@example.com",
    "!def!xyz%abc@example.com",
    "_Yosemite.Sam@example.com",
    "~@example.com",
    "example-indeed@strange-example.com",
    "test/test@test.com",
    "admin@mailserver1"
]

# Example phone numbers to test
example_phone_numbers = [
    "123-456-7890",
    "098-765-4321", 
    "555-555-5555",
    "1234567890",
    "9876543210",
    "111-222-3333",
    "444-555-6666",
    "777-888-9999",
    "000-111-2222",
    "3334445555"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_name(name):
    return bool(re.match(r'^[A-Za-z]+( [A-Za-z]+)?$', name))

def validate_email(email):
    return bool(re.match(r'^[\w.%+-]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}$', email))

def validate_phone_number(phone_number):
    return bool(re.match(r'^\d{3}-?\d{3}-?\d{4}$', phone_number))

def clean_name(name):
    # Remove any characters that are not alphabetic or spaces
    cleaned_name = re.sub(r'[^A-Za-z\s]', '', name)
    # Remove extra spaces
    cleaned_name = re.sub(r'\s+', ' ', cleaned_name).strip().title()
    return cleaned_name

def format_phone_number(phone_number):
    # Remove any non-numeric characters
    digits = re.sub(r'\D', '', phone_number)
    # Format the digits with dashes
    formatted_number = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', digits)
    return formatted_number

# Contact class
# Create a class called 'Contact' to represent individual contact.
# The Contact class should have the following features.

# - properties
#    - name
#    - phone_number
#    - email
# - methods
#    __str__ method that uses and f string to print out all contact attributes cleanly.
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, number: {self.phone_number}, email: {self.email}"
    
class BusinessContact(Contact):

    def __init__(self, name, phone_number, email, company, job_title):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.company = company
        self.job_title = job_title

# ContactBook class
# Create a class called 'ContactBook' to represent a group of contacts. It should have the following features.
# - properties
#    - contacts - a list containing all available contacts
# - methods
#    - add_contact - takes in and adds a new contact
#    - delete_contact - deletes the contact
#    - search_contact(name): bool - returns true if there is a contact with the input name.
#    - display_contacts - prints out all of the contacts in your Contact list.
class ContactBook:
    def __init__(self):
        self.contacts = [Contact("bob", phone_number="801-123-1234", email="bob@gmail.com")]

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if len(self.contacts) == 0:
            print("You contact book is empty")
        for contact in self.contacts:
            print(contact)


def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Ask for a new contact name
            while True: 
                name = input("Enter name: ")
                if validate_name(name):
                    name = clean_name(name)
                    break
                else:
                    print("Invalid name. Please try again.")
            pass
            # Ask for a new contact phone number
            while True: 
                phone_number = input("Enter phone number: ")
                if validate_phone_number(phone_number):
                    phone_number = format_phone_number(phone_number)
                    break
                else:
                    print("Invalid phone number. Please try again.")
            pass
            # Ask for a new contact email
            while True: 
                email = input("Enter email: ")
                if validate_email(email):
                    break
                else:
                    print("Invalid email. Please try again.")
            pass
            contact = BusinessContact(name, phone_number, email)
            contact_book.add_contact(contact)
            clear_screen()
            print(f"Successfully added {contact} as a new contact!!")
        elif choice == "2":
            name = input("Enter a name for a contact to delete: ")
            did_delete_contact = contact_book.delete_contact(name)
            if did_delete_contact:
                clear_screen()
                print(f"Deleted a contact named {name}")
            else:
                clear_screen()
                print(f"No contact named {name} found to delete.")
        elif choice == "3":
            name = input("Enter a name to search for: ")
            contact_found = contact_book.search_contact(name)
            if contact_found:
                clear_screen()
                print("Found a contact!")
                print(contact_found)
            else:
                clear_screen()
                print("No contact found.")
        elif choice == "4":
            clear_screen()
            print("Here are all your contacts.")
            contact_book.display_contacts()
        elif choice == "5":
            break
        else:
            clear_screen()
            print("Please enter a valid option")


if __name__ == "__main__":
    clear_screen()
    main()