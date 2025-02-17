import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# value = roll()
# print(value)  # random number between 1 and 6

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be a number between 1 and 4.")
    else:
        print("Invalid input.")

print("The number of players is: ", players)  # number of players

max_score = 50
# list of player scores initialized to 0 for each player syntax = [0 for _ in range(4)}
player_scores = [0 for _ in range(players)]

print(player_scores)  # list of player scores3

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number ", player_idx + 1, "Your turn.\n")
        print("Your current score is: ")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll the dice? (y or n): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("\nOh no! You rolled a 1! \nNo points for you, your turn is now over.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your score is: ", current_score)
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])
