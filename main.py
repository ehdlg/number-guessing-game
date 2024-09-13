from random import random

DIFFICULTY = {
    1: {"name": "Easy", "chances": 10},
    2: {"name": "Medium", "chances": 5},
    3: {"name": "Hard", "chances": 3},
}
NUMBER_TO_GUESS = round(random() * 101)
VALID_DIFFICULTY_INPUTS = (1, 2, 3)

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n
""")

while True:
    try:
        difficulty_input = int(input("Enter your choice:"))

        if difficulty_input in VALID_DIFFICULTY_INPUTS:
            break

        print("\nEnter a valid difficulty level\n")
    except ValueError:
        print("\nPlease enter a valid number\n")


print(
    f"Great! You have chosen {DIFFICULTY.get(difficulty_input).get('name')} difficulty level\nLet's start the game!\n\n"
)

CHANCES = DIFFICULTY.get(difficulty_input).get("chances")
attempt_count = 0

while True:
    try:
        print(f"ATTEMTP {attempt_count + 1}")

        guess = int(input("Enter your guess: "))

        if guess == NUMBER_TO_GUESS:
            print("Correct!\n")
            print(
                f"Congratulations! You guessed the number in {attempt_count + 1} attempts"
            )
            break

        distance = "lesser" if guess > NUMBER_TO_GUESS else "greater"

        print(f"Incorrect! The number is {distance} than {guess}\n")

        attempt_count += 1

        if attempt_count == CHANCES:
            print("Defeat!\n")
            break

    except ValueError:
        print("That's not an integer!!\n")
        attempt_count += 1

exit()
