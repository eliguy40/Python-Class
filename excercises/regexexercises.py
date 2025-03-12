import re

# Fruit Text for exercises 1-6
fruit_text = "I have an apple, a banana, and another apple."
# Exercise 1: Using re.search
# Find the first occurrence of the word "apple" in the fruit_text
search_apple = re.search(r"apple", fruit_text)
print(search_apple.group())

# Exercise 2: Using re.findall
# Find all occurrences of the word "apple" in the fruit_text
findall_apple = re.findall(r"apple", fruit_text)
print(findall_apple)

# Exercise 3: Using re.search with a more complex pattern
# Find the first occurrence of a word that starts with 'b' and ends with 'a' in the fruit_text
b_a_search = re.search(r"(?:\s|^)(b\w+a)\b", fruit_text)
print(b_a_search.group(1))

# Exercise 4: Using re.findall with a more complex pattern
# Find all words that start with 'a' and end with 'e' in the fruit_text
b_a_findall = re.findall(r"(?:\s|^)(a\w+e)\b", fruit_text)
print(b_a_findall)

# Exercise 5: Using re.search with groups
# Find the first occurrence of a word that starts with 'a' and capture the word in the fruit_text


# Exercise 6: Using re.findall with groups
# Find all words that start with 'a' and capture the words in the fruit_text

# Phone Text for exercises 7-8
phone_text = "My phone number is 123-456-7890."
# Exercise 7: Using re.search with a digit pattern
# Find the first occurrence of a digit in the phone_text


# Exercise 8: Using re.findall with a digit pattern
# Find all occurrences of digits in the phone_text

# Mary text for exercises 9-10
mary_text = "My name is Mary and I live in Miami."
# Exercise 9: Using re.search with a word boundary pattern
# Find the first occurrence of a word that starts with 'M' and ends with 'y' in mary_text


# Exercise 10: Using re.findall with a word boundary pattern
# Find all words that start with 'M' and end with 'y' in mary_text


# Email text for exercises 11-12
email_text = "Please contact us at support@example.com or sales@example.com."
# Exercise 11: Using re.search with an email pattern
# Find the first occurrence of an email address in the email_text


# Exercise 12: Using re.findall with an email pattern
# Find all occurrences of email addresses in the email_text

