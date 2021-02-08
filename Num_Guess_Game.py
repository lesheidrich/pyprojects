import random
logo = """
..%%%%...%%..%%..%%%%%%...%%%%....%%%%...........%%%%%%..%%..%%..%%%%%%..........%%..%%..%%..%%..%%...%%..%%%%%...%%%%%%..%%%%%..
.%%......%%..%%..%%......%%......%%................%%....%%..%%..%%..............%%%.%%..%%..%%..%%%.%%%..%%..%%..%%......%%..%%.
.%%.%%%..%%..%%..%%%%.....%%%%....%%%%.............%%....%%%%%%..%%%%............%%.%%%..%%..%%..%%.%.%%..%%%%%...%%%%....%%%%%..
.%%..%%..%%..%%..%%..........%%......%%............%%....%%..%%..%%..............%%..%%..%%..%%..%%...%%..%%..%%..%%......%%..%%.
..%%%%....%%%%...%%%%%%...%%%%....%%%%.............%%....%%..%%..%%%%%%..........%%..%%...%%%%...%%...%%..%%%%%...%%%%%%..%%..%%.
.................................................................................................................................                                                                                                                                                    
"""


def maxtries_guessno(atmpt, ans_max):
    """Prints answer range, returns max tries and guess number as answer"""
    print(f"\nI'm thinking of a number between 1 and {ans_max}")
    max_tries = atmpt
    ans_gen = random.randint(1, 50)
    return max_tries, ans_gen, ans_max


def game_setup():
    """Initializes game with difficulty selector, and allowed attempts based on that.
       Guess number (answer) is also selected by calling maxtries_guessno()"""
    print("\n******************************************************************************")
    print(logo)
    print("Welcome to The Number Guessing Game!")
    #user choose difficulty or exit
    difficulty = int(input("Choose a difficulty level, press:\n  1 - easy\n  2 - hard\n>> "))
    while (difficulty!=1) and (difficulty!=2):
        difficulty = int(input("Input error, please press:\n  1 - easy\n  2 - hard\n>> "))
    #setup max attempts based on chosen difficulty
    #answer = guess number
    if difficulty == 1:
        attempts, answer, ans_max = maxtries_guessno(10, 50)
    elif difficulty == 2:
        attempts, answer, ans_max = maxtries_guessno(5, 100)
    else:
        print("Error: level selection")
    return attempts, answer, ans_max


if __name__ == '__main__':
    while True:
        tries, ans, max_val = game_setup()
        wrong = []
        while tries > 0:
            print(f"Tries left: {tries}")
            guess = int(input(f"Guess the number (0 to exit)>> "))
            if guess == 0:
                print(f"\nThank you for playing.\nYour number was {ans}")
                break
            elif guess > max_val:
                print("\nYou can't guess a number greater than the maximum value.")
            elif guess < 1:
                print("\nPlease guess a number greater than 0.")
            elif guess in wrong:
                print("\nYou tried that number already. Try another one")
            elif guess == ans:
                print(f"\nCONGRATULATION!!!\nYOU WIN!!!\nYou guessed correctly, "
                      f"you had {tries} tries left.")
                break
            else:
                tries -= 1
                wrong.append(guess)
                if guess > ans:
                    print("\nThat number is TOO BIG.")
                else:
                    print("\nThat number is TOO SMALL.")
                print("Attempted numbers:", ", ".join(str(num) for num in wrong))
        if tries == 0:
            print(f"\nYOU LOSE.\nYour number was {ans}")

        play_again = input("Press 'q' to quit, 'enter' to play again>> ").lower()
        if play_again == 'q':
            print("Goodbye!\n\n")
            break
