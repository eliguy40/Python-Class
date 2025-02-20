# Used for Gemini's email grapher
import matplotlib.pyplot as plt
import numpy as np
###

def eng2sp_dictionary():
    eng2sp = dict()
    # eng2sp["one"] = "uno"
    eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    # {"key": "value"}
    # it doesn't matter what order the dictionary is in because
    # you just look up the value with the key
    print(eng2sp)

    print(eng2sp['one'])

# Uses a dictionary to count how many letters are in a string. Basically a histogram
# Made by google gemini
def count_characters(text):
    char_counts = {}  # Initialize an empty dictionary
    for char in text:
        if char in char_counts:
            char_counts[char] += 1  # Increment count if character exists
        else:
            char_counts[char] = 1  # Add character with count 1 if it's new
    return char_counts

# This uses the .get() command and makes this way easier and quicker
def count_characters_concise(text):
    dictionary = dict()
    for character in text:
        dictionary[character] = dictionary.get(character,0) + 1
    return(dictionary)

# text = "this is a crazy string lol and i wonder how many letters there will be"
# count_text = count_characters_concise(text)
# print(count_text)

# Docs: https://books.trinket.io/pfe/09-dictionaries.html#dictionaries

# def count_days_of_week_bad():
#     mbox = "/home/elijah/Documents/code/Python-Class/mbox.txt"

#     file_handle = open(mbox, "r")

#     dictionary = dict()
#     for line in file_handle:
#         words = line.rstrip()
#         print(words)
#         if words[0] == "From":
#             dictionary[words[2]] = dictionary.get(words[2], 0) + 1
#     print(dictionary)

def count_days_of_week(filename):
    days_counter = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                words = line.strip().split()
#                print(words)
                day = words[2]
                days_counter[day] = days_counter.get(day, 0) + 1

    return days_counter

def count_emails(filename):
    email_counter = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                words = line.strip().split()
#                print(words)
                emails = words[1]
                email_counter[emails] = email_counter.get(emails, 0) + 1

    return email_counter

def graph_email_counts(email_counts):
    """
    Generates a terminal-based graph of email counts from a dictionary.

    Args:
        email_counts: A dictionary where keys are email addresses (or labels)
                      and values are the corresponding counts.
    """

    if not email_counts:
        print("No email data provided.")
        return
    
    emails = list(email_counts.keys())
    counts = list(email_counts.values())

    # Sort for better visualization (optional but often helpful)
    sorted_indices = np.argsort(counts)
    emails = [emails[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]


    # Terminal-based plotting (using character-based bars)
    max_count = max(counts)
    bar_width = 40  # Adjust bar width as needed

    print("-" * (bar_width + 20)) # Top border

    for email, count in zip(emails, counts):
        bar_length = int((count / max_count) * bar_width)
        bar = "#" * bar_length # Use whatever character you prefer for the bars
        print(f"{email:20} | {bar} {count}") # Email label and bar

    print("-" * (bar_width + 20)) # Bottom border
    print(f"Total Emails: {sum(counts)}") # Optional: Display the total count

    # Optional: Matplotlib for nicer graphs (if you have it installed)
    # try:
    #     plt.barh(emails, counts)
    #     plt.xlabel("Count")
    #     plt.ylabel("Email")
    #     plt.title("Email Counts")
    #     plt.tight_layout() # Adjust layout to prevent labels from overlapping
    #     plt.show() # Display the plot
    # except ImportError:
    #     print("\nMatplotlib not found. Install it for richer plots: pip install matplotlib")
    # except Exception as e: # Catch any matplotlib related errors
    #     print(f"\nError creating matplotlib graph: {e}")

def most_emailed(emails):

    highest_key = None
    highest_number = float("-inf")

    for key, value in emails.items():  # Iterate through key-value pairs
        if isinstance(value, (int, float)):
            if value > highest_number:  # Direct comparison
                highest_number = value
                highest_key = key
        else:
            print("your value is not an int")
    
    print(f"Most emailed: {highest_key} \nAmount of emails: {highest_number}")

def email_domain_counter(filename):
    domain_counter = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                words = line.strip().split()
                email_address = words[1]
                domains = email_address.split("@")[1]
                # print(domains)
                domain_counter[domains] = domain_counter.get(domains, 0) + 1

    return domain_counter

days_of_week = count_days_of_week("/home/elijah/Documents/code/Python-Class/mbox.txt")
email_choice = input("Open mbox or your own file? (mbox/custom)\n").upper()

if email_choice == "MBOX":
    emails = count_emails("/home/elijah/Documents/code/Python-Class/mbox.txt")
elif email_choice == "CUSTOM":
    emails = input("enter your file (with path) below:\n")
else:
    print("sorry, please input a correct respone.")
    quit()

action = input("What would you like to do with said file?\n1. Graph email count\n2. Show most contacted email\n3. Count email domains\n")

if action == "1":
    graph_email_counts(emails)
elif action == "2":
    most_emailed(emails)
elif action == "3":
    print(email_domain_counter("/home/elijah/Documents/code/Python-Class/mbox.txt"))
else:
    print("Either incorrect number was inputed or no input at all.")
    quit()
