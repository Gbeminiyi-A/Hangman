# Create hangman CLI


WORD = "HANGMAN"


def game():
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


if __name__ == "__main__":
    game()
