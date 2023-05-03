rounds = ""
input("How many rounds? ")
response = rounds

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print(f"*** Round # {rounds_played} ***")
    rounds -= 1
    print(f"Rounds: {rounds}")
    print()

    # prevent balance from going into negatives
    if rounds < 1:
        play_again = 'xxx'
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final balance", rounds)
