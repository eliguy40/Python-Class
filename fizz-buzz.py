# This code is supposed to say Fizz if the number is divisible by 3, Buzz if it's divisible by 5,
# and Fizz Buzz if divisible by both. 

user = input("Input:\n")
user = int(user)
for user in range(1, user + 1):
    if user % 3 == 0:
        if user % 5 != 0:
            print("Fizz")
        elif user % 5 == 0:
            print("Fizz Buzz")
    elif user % 5 == 0:
        if user % 3 != 0:
            print("Buzz")
        elif user % 3 == 0:
            print("Fizz Buzz")
    else:
        print(user)