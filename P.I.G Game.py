# roll the die, u get a number between 1 and 6.
# If we get any number other than 1, we add the previous number to the running score.
# we can roll any no. of times.

# SETTING UP A ROLLING DICE
import random

def myroll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
# Setting up VALID No. of Players
while True:
    players = int(input("enter the number of players(1-4)"))
    if 2 <= players <= 4:
        break
    elif 2<= players or 4>= players:
        print("must be in between 2 and 4 players")
    else:
        print("invalid, try again")

max_score = 50 # tentative
player_scores = [0 for i in range(players)] # loops over the entire no. of players and gives the inital score for all of them.

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        print("your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll(y/n)").lower()
            if should_roll != "y":
                break

            value = myroll()
            if value == 1:
                print("you rolled a 1! Turn finished")
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("your score is:", current_score)

        player_scores[player_idx] += current_score
        print("your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx +1,
      "is the winner with a score of:", max_score)
