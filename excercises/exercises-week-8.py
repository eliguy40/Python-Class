# Exercise 1
def nameAge():
    name = input("Enter Name:\n")
    age = input("Enter Age:\n")
# Exercise 2
def maxNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1, "is the highest number")
    if num2 > num1 and num2 > num3:
        print(num2, "is the highest number")
    if num3 > num2 and num3 > num1:
        print(num3, "is the highest number")
def easyMaxNumber(*nums):
    return max(nums)

def printArgs(*print_args):
    print("Printing Values")
    for nums in print_args:
        print(nums)
# Exercise 4
def addArgs(*numbers):
  total = 0
  for number in numbers:
    total += number
  print(total)
def easyAddArgs(*args):
    return sum(args)
# Exercise 5

# printArgs(15, 12)
# addArgs(12, 15, 20)

# Exercise 7
def calculation(num1, num2):
    return num1 + num2, num1 - num2

def show_employee(name, salary = 9000):
    print(f"{name} gets paid {salary}")

# print(calculation(12, 24))
show_employee("Josh", 10)