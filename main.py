print("Hello Candidate, And Welcome to the guessing game!")
secret_number = 1442
guess_number = int(input("Please insert your guess number: "))

if guess_number == secret_number:
    print("Congratulations! You guessed the secret number!")
else:
    print("Sorry, that's not the secret number. Try again!")

