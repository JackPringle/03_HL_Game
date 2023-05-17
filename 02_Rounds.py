# Functions

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


rounds = int_check("How many rounds? ", 0)
response = rounds

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # Print round number

    print(f"*** Round # {rounds_played} ***")
    rounds -= 1
    print(f"Rounds: {rounds + 1}")
    print()

    # prevent balance from going into negatives
    if rounds < 1:
        play_again = 'xxx'
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final balance", rounds)
