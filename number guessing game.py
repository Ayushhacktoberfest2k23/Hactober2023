import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of attempts
attempts = 0
max_attempts = 5

# Game loop
while attempts < max_attempts:
    try:
        # Get user input
        guess = int(input("Guess the secret number (between 1 and 100): "))
        attempts += 1

        # Compare the guess with the secret number
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        if attempts == max_attempts:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

    except ValueError:
        print("Please enter a valid number.")

