
def main():
    filename = input("What file would you like to open?")
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

if __name__ == "__main__":
    main()
