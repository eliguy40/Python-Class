try:
    fhand = input("What is the name of your file?")

except:
    print("Sorry, that file name is incorrect")

count = 0

for line in fhand:
    count = count + 1
print('Line Count:', count)
