def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
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


low_number = 1
high_number = 10

rounds_won = 0

secret = 7

# Start Round!!
while True:

    secret = 8

    guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
    print("you guessed", guess)

    if guess == "xxx":
        end_game = "yes"
        break

        # compare guess to secret number
    elif guess < secret:
        print("Too low!")

    elif guess > secret:
        print("Too high!")

    if guess == secret:
        rounds_won += 1
        break
