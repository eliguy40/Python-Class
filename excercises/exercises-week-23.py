import re

def count_timeofday(filename):
    timeofday_counter = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                words = line.strip().split()
#                print(words)
                timeofday = words[5]
                hour = timeofday.split(":")[0]
                # print(hour)
                timeofday_counter[hour] = timeofday_counter.get(hour, 0) + 1

    t_list = list()
    for k,v in timeofday_counter.items():
        t_list.append((k,v))
    t_list.sort(reverse=False)
    for line in t_list: print(line[0], line[1])

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

def highest_dict_value(mail):
    t_list = list()
    for k,v in mail.items():
        t_list.append((v,k))
    t_list.sort(reverse=True)
    
    highest_v, highest_k = t_list[0]

    return highest_k, highest_v

def count_letters(filename):
    letter_counter = {}
    with open(filename, 'r') as file:
        for line in file:
            cleaned_line = re.sub(r'[^a-zA-Z]', '', line).lower()
            # print(cleaned_line)
            letters = list(cleaned_line)
            for letter in letters:
                letter_counter[letter] = letter_counter.get(letter, 0) + 1
    
    t_list = list()
    for k,v in letter_counter.items():
        t_list.append((k,v))
    t_list.sort(reverse=False)
    for line in t_list: print(line[0], line[1])
path = "/home/elijah/Documents/code/Python-Class/mbox.txt" #input("File: ")

#highest_mail_vk = highest_dict_value(count_emails(path))
# print(count_emails(path))
# count_timeofday(path)
count_letters(path)