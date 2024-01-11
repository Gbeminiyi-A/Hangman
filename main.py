# Create hangman CLI
import sys

WORD = "HANGMAN"

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
    fails = 0
    print(f"There are {len(WORD)} letters in this word.")
    while fails < 5:
        user_guess()
        fails += 1
    print(f"The correct word is {WORD}")


def catch_fails(fails):
    print(HANGMAN_PICS[fails - 1])


def user_guess():
    letter = input("Enter a letter: ").upper()
    if letter in WORD:
        if letter in correct_guess:
            print("You have entered this letter before, Try again")
            user_guess()
        else:
            correct_guess.append(letter)
            print(True)
    else:
        if letter in missed_letters:
            print("You have entered this letter before, Try again")
        else:
            missed_letters.append(letter)
    print(f"You've entered {', '.join(correct_guess)} {', '.join(missed_letters)}")


def check_remaining(letter_input):
    position = []
    for letter in WORD:
        if letter_input == letter:
            position.append(WORD.find(letter_input))


if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        sys.exit()
