import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts remaining.")
            else:
                print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("Thanks for playing!")
if __name__ == "__main__":
    guess_the_number()
