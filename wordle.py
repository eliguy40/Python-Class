import random

class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def choose_secret_word():
    word_list = ["apple", "berry", "mango", "peach", "grape"]
    return random.choice(word_list)

def display_colored_guess(guessed_word, secret_word):

    for letter_index in range(len(guessed_word)):
        letter = guessed_word[letter_index]
        printed_letter = []
#     b. If the letter is in the same spot in both guessed_word and the secred_word then color it Green.
        if letter == secret_word[letter_index]:
            print(colors.GREEN + letter + colors.END, end = '')
#     c. If the letter from guessed_word is IN secred_word then color it Yellow.
        elif letter in secret_word:
            print(colors.YELLOW + letter + colors.END, end = '')
#     d. else color it normal (black/white).
        else:
            print(letter, end='')
#     e. Print the colored word (and eventually previous guesses)
    print()

def wordle():
    print("Welcome to wordle!!!")
    # 1. Pick a random word from a list of words (ideally a super large list/dictionary)
    secret_word = choose_secret_word()
    # TODO: Comment out this print statement before finishing.
    # print(secret_word)

    remaining_guesses = 6
    while remaining_guesses > 0:
        # 2. Prompt the user for a 5-letter word and validate
        guessed_word = input("Guess your 5-letter word: ")
        #     a. lowercase the input word
        guessed_word = guessed_word.lower()
        #     b. Make sure there are only letters.
        if not guessed_word.isalpha():
            print("Invalid word please try with only letters.")
        #     c. Make sure the guessed_word is only 5 characters long.
        elif len(guessed_word) != 5:
            print("Your word is the wrong length please try again.")
        #     d. Enhancement - Make sure the guessed_word is a valid word.
        else:
            remaining_guesses -= 1
            # We have a valid word.
            print(f"You have a valid guess: {guessed_word}")
            # 3. Compare the guessed_word with the secret_word.
            #     a. If the guessed_word equals the secret_word then they win! Game Over!
            if guessed_word == secret_word:
                print("You guessed the correct word! You win!!")
                break
            else:
                display_colored_guess(guessed_word, secret_word)
            print(f"You guessed incorrectly, you have {remaining_guesses} tries left.")
        # 4. If the guess wasn't correct then we let the guess again and decrease their remaining attempts.


if __name__ == "__main__":
    wordle()