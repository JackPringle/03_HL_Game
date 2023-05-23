import random


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
                if response > low:
                    return response

            print(error)

        except ValueError:
            print(error)


# Main Routine...

# Welcome statements
print()
print("---------------------------------------------------")
print("WELCOME TO HIGHER LOWER GAME BY JACK PRINGLE!")
print("---------------------------------------------------")
print()

# Display instructions

print("Games Instructions... ")
print()
print("Enter how many rounds you would like to play.")
print("If you would like, you can press <enter> for continuous mode.")
print("For each round, you will have to guess for a number between 0 and 100 inclusive.")
print("Each round you get 6 attempts to guess the secret number.")
print("If at any point you wish to quit, type <xxx>")
print("Good luck guessing and HAVE FUN!")
print()
print("----------------------------")
print("START OF GAME")
print("----------------------------")

lowest = 0
highest = 100

max_guesses = 6

rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 100

mode = "regular"

rounds = int_check("How many rounds?: ", 0, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop...
end_game = "no"
while end_game == "no" and rounds_played < rounds:

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    secret = random.randint(lowest, highest)
    guesses_allowed = max_guesses
    guesses_left = guesses_allowed
    already_guessed = []

    # Start  guessing!

    guess = ""

    while guess != secret and guesses_left >= 1:

        guess = int_check("Guess: ", lowest, highest, "xxx")
        print()

        if guess == "xxx":
            end_game = "yes"
            break

        # checks that guess is not duplicate
        if guess in already_guessed:
            print("You already guessed that number! Please try again.")
            print(f"You *still* have {guesses_left} guesses left")
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < secret:
                print(f"TOO LOW, try a higher number.")
                print()
                print(f"Guesses left: {guesses_left}")
                print()

            elif guess > secret:
                print(f"TOO HIGH, try a lower number.")
                print()
                print(f"Guesses left: {guesses_left}")
                print()

        else:
            if guess < secret:
                print("Too Low!")
            elif guess > secret:
                print("Too High!")

        if guess == secret and rounds != 0:
            print("Well done, you got it!")
            print(f"The secret number was {secret}!")
            print("----------------------------")
            print(f"End of round {rounds_played}!")
            print("----------------------------")

    if guesses_left == 0 and rounds_played == rounds:
        print("----------------------------")
        print("NO MORE GUESSES!")
        print("----------------------------")
        print(f"The secret number was {secret}!")

        break

# end game thanks
print("---------------------------------------------")
print("THANKS FOR PLAYING HIGHER LOWER GAME!")
print("---------------------------------------------")
