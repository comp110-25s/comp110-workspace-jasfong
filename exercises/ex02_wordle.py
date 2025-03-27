"""Creating Wordle"""

__author__ = "730719749"


def contains_char(search: str, character: str) -> bool:
    """True if the single character of the second string is found"""
    assert len(character) == 1, f"len('{character}') is not 1"

    ind: int = 0
    flag = False
    while ind < len(search):
        if search[ind] == character:
            flag = True
        ind += 1
    return flag


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji that codifies the results of the guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    ind: int = 0
    result: str = ""

    while ind < len(guess):
        if guess[ind] == secret[ind]:
            result += GREEN_BOX
        elif contains_char(secret, guess[ind]) == True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        ind += 1
    return result


def input_guess(expected: int) -> str:
    """Prompts for the correct character length"""
    word: str = input("Enter a " + str(expected) + " character word:")
    while len(word) != expected:
        word = input("That wasn't " + str(expected) + " chars! Try again:")
    return word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    word: int = len(secret)
    turns: int = 1
    while turns <= 6:
        print("=== Turn " + str(turns) + "/6 ===")
        guess: str = input_guess(word)
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(turns) + "/6 turns!")
            turns = 100
        turns += 1
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
