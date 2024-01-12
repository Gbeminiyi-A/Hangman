# Create hangman CLI
import sys

WORD = "HANGMAN"
guessed_word = "-" * len(WORD)
position = []
word = list(WORD)
guessed = list(guessed_word)

HANGMAN_PICS = [r"""
  +--+
  |  |
     |
     |
     |
     |
 =====""",
                r"""
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",
                r"""
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",
                r"""
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",
                r"""
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",
                r"""
   +--+
   |  |
   O  |
  /|\ |
  /   |
      |
  =====""",
                r"""
   +--+
   |  |
   O  |
  /|\ |
  / \ |
      |
  ====="""]

missed_letters = []
correct_guess = []


def intro():
    print(
        """
        _
        | |
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/
        """)
    print("-" * len(WORD))


def game():
    intro()
    print(f"There are {len(WORD)} letters in this word. \n")
    user_guess()

    print(f"The correct word is {WORD}")


def catch_fails(fails):
    print(HANGMAN_PICS[fails - 1])


def user_guess():
    fails = 0
    while fails < 7:
        letter = input("Enter a letter: ").upper()
        if letter in WORD:
            if letter in correct_guess:
                print("You have entered this letter before, Try again\n")
            else:
                correct_guess.append(letter)
                show_guess(letter)
        else:
            if letter in missed_letters:
                print("You have entered this letter before, Try again\n")
            else:
                missed_letters.append(letter)
                print("The letter you have entered is not in the word.")
                print(HANGMAN_PICS[fails])
                fails += 1
        print(f"You've entered {', '.join(correct_guess)}, {', '.join(missed_letters)}\n")


def show_guess(letter_input):
    global guessed
    for i in word:
        if letter_input == i:
            index = word.index(i)
            guessed[index] = letter_input
    print("".join(guessed))


if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        sys.exit()
