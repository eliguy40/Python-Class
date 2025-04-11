import re

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
    cleaned_name = re.sub(r'\s+', ' ', cleaned_name).strip()
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

nate = Contact("Nate", "801-234-2345", "nate@gmail.com")
print(nate)

vincent = Contact("Vincent", "801-234-8765", "vincent@gmail.com")
print(vincent)

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
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return True
        return False

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

my_contacts = ContactBook()
my_contacts.add_contact(nate)
print(my_contacts.contacts)
my_contacts.delete_contact("Vincent")
print(my_contacts.search_contact("Vincent"))
print(my_contacts.search_contact("Nate"))

my_contacts.add_contact(vincent)

my_contacts.display_contacts()


