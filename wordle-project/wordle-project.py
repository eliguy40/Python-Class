import random
import os

class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def choose_secret_word():
#   This is usually best practice to find the file because now it
#   doesn't matter where you run the .py file
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "fiveLetterWords.txt")

#   use for troubleshooting in case of os path error stuffs
#    print(f"current_dir is: {current_dir}")

    word_list = []
    file_handle = open(file_path)
#   this for loop grabs each word and makes a new word list
#   that sorts them out easier
    for line in file_handle:
        word = line.rstrip()
        if len(word) == 5:
            word_list.append(word)

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
    win_streak = "open"

    print(f"Welcome to wordle!!! Your current win streak is... {high_score(win_streak)}!")
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
        #     d. TODO: fix this --> Enhancement - Make sure the guessed_word is a valid word.
        #elif guessed_word not in word_list:
        #                print("Your word is not in the dictionary. Please try again.")

        else:
            remaining_guesses -= 1
            # We have a valid word.
            print(f"You have a valid guess: {guessed_word}")
            # 3. Compare the guessed_word with the secret_word.
            #     a. If the guessed_word equals the secret_word then they win! Game Over!
            if guessed_word == secret_word:
                win_streak = True
                print(colors.GREEN + guessed_word + colors.END, end = '')
                print("\nYou guessed the correct word! You win!!")
                print(f"Your current streak is... {high_score(win_streak)}!")
                quit()
            elif remaining_guesses == 0:
                print(f"Sorry, you lost! The secret word was...")
                print(colors.GREEN + secret_word + colors.END, end = '')
                win_streak = False
                print(f"\nStreak reset to... {high_score(win_streak)}! :(")
                quit()
            else:
                display_colored_guess(guessed_word, secret_word)
            print(f"You guessed incorrectly, you have {remaining_guesses} tries left.")
        # 4. If the guess wasn't correct then we let the guess again and decrease their remaining attempts.
        

def high_score(win_streak):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "highScore.txt")

    # Read the existing score (default to 0 if the file doesn't exist or is empty)
    try:
        with open(file_path, "r") as file_handle:
            high_score = int(file_handle.read().strip() or 0)
    except FileNotFoundError:
        print("cannot find file: highScore.txt")

    # Update the score based on winlose
    if win_streak == True:
        new_score = high_score + 1 
    elif win_streak == "open":
        return high_score
    else:
        new_score = 0

    # Write the new score to the file
    with open(file_path, "w") as file_handle:
        file_handle.write(str(new_score))
    
    return new_score

if __name__ == "__main__":
    wordle()
