
def exercise_0():
    filename = input("Enter path and file name to open:")
    count = 0
    try:
#        this try command is to make sure that the file actually exists
        fhand = open(filename)
        for line in fhand:
            line = line.rstrip()
            if line.startswith("X-Content-Type"):
                count = count + 1
                print(line)
        print(f"There were {count} X-Content-Type lines in {filename}")

    except FileExistsError:
        print(f"The file {file_name} does not exist.")

def exercise_1():
    filename = input("Enter path and file name to open:")
    try:
#        this try command is to make sure that the file actually exists
        fhand = open(filename)
        for line in fhand:
            print(line.upper())

    except FileExistsError:
        print(f"The file {file_name} does not exist.")

def exercise_2_3():
    filename = input("Enter path and file name to open:")
    count = 0
    dspam_average = 0
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        try:
#           this try command is to make sure that the file actually exists
            fhand = open(filename)
            for line in fhand:
                line = line.rstrip()
#               pulls each line starting with the string below and 
#               finds the average spam confidence
                if line.startswith("X-DSPAM-Confidence:"):
                    num = line.split(':')[1].strip()
                    dspam_average = float(num) + dspam_average
                    count += 1
            final_dspam_average = dspam_average / count
            print(f"Average spam confidence: {final_dspam_average}")

        except FileExistsError:
            print(f"The file {file_name} does not exist.")

if __name__ == "__main__":
    exercise_2_3()
