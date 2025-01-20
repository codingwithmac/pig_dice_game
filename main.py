import random

def roll(): # creating roll function for rolling the die
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True: # asks how many players playing the game.
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players) #converts string to integer after being checked if input is a digit
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players.")

    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players)] # list comprehension

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1} has just started!\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y": #converts to lowercase
                break

            value = roll()
            if value == 1:
                print("You rolled 1. Turn over.")
                break
            else:
                current_score += value
                print(f"You rolled a: {value} ")

            print(f"Your score is: {current_score}")
        player_scores[player_idx] += current_score
        print(f"Your total score is: {player_scores[player_idx]}")