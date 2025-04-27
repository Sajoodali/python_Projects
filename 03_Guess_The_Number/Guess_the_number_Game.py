import random


guess_number = random.randint(1,100)

while True:
    try:
        user_input = int(input("Guess a number between 1 and 100: "))
        if user_input < guess_number:
            print("Too low! Try again.")
        elif user_input > guess_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")