# Functions...

# Checks an integer is valid (more than low, less than high)
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

            print(error)

        except ValueError:
            print(error)


# Main Routine...

rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 100

mode = "regular"

rounds = int_check("How many rounds?: ", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop...
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    SECRET = 7
    GUESSES_ALLOWED = 5
    guesses_left = GUESSES_ALLOWED
    already_guessed = []

    # Start  guessing!

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
        break

