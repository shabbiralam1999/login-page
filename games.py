import random

# computer selects a random number between 1 and 50
secret_number = random.randint(1, 50)

print("Guess the number (between 1 and 50)!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed it!")
        break
