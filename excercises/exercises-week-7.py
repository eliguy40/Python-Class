# Exercises 2 & 3
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Excercise 4 is answer d

# Excercise 5 is answer d

# Excercise 6
try:
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    def computepay(hrs, rate):
        if hrs > 40:
            print("Good job working overtime! You get %50 more pay while you were working overtime!")
            hrs = hrs - 40
            return hrs * rate * 1.5 + 40 * rate
        if hrs < 40:
            print("Here's your how much you made:")
            return hrs * rate
    print('Pay:', computepay(hrs, rate))
except:
    print("That doesn't work. Please input an integer or string!")

# Is Excercise 6.4 just the same as Excercise 6?