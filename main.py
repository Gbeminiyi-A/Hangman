# Create hangman CLI
import sys

WORD = "HANGMAN"


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


def game():
    intro()
    fails = 0
    while fails < 5:
        print(f"There are {len(WORD)} letters in this word.")
        letter = input("Enter a letter: ").upper()
        if letter in WORD:
            print("Correct")
        else:
            print("fail")
            fails += 1
    print(f"The correct word is {WORD}")


def catch_fails(fails):
    if fails == 1:
        print("")


if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        sys.exit()
