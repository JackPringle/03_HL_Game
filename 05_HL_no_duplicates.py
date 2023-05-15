# HL component 5 - no duplicates

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 5 - Prevents duplicate guesses

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function

    # checks that guess is not duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again.")
        print(f"You *still* have {guesses_left} guesses left")
        continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < SECRET:
                print(f"Too low, try a higher number. Guesses left: {guesses_left}")

            elif guess > SECRET:
                print(f"Too high, try a lower number. Guesses left: {guesses_left}")

        else:
            if guess < SECRET:
                print("Too Low!")
            elif guess > SECRET:
                print("Too High!")

    if guess == SECRET:
        if guesses_left == GUESSES_ALLOWED:
            print("Amazing! You got it! ")
        else:
            print("Well done, you got it!")
