# HL component 5 - Prevents duplicate guesses

# Functions...

# Integer checker
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"

    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too high etc...)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            else:
                print(error)

        except ValueError:
            print(error)


SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int_check("Guess: ")
    print()

    # checks that guess is not duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again.")
        print(f"You *still* have {guesses_left} guesses left")
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print(f"TOO LOW, try a higher number.")
            print()
            print(f"Guesses left: {guesses_left}")
            print()

        elif guess > SECRET:
            print(f"TOO HIGH, try a lower number.")
            print()
            print(f"Guesses left: {guesses_left}")
            print()

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

if guesses_left == 0:
    print()
    print("----------------------------")
    print("NO MORE GUESSES!")
    print("----------------------------")
