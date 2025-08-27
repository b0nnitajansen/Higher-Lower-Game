import game_data
import art
import random

print(art.logo)

# Pick 2 random items
randomSample = random.sample(game_data.data, 2)

print(f"Compare A: {randomSample[0]['name']}, {randomSample[0]['description']}, {randomSample[0]['country']}")
print(art.vs)
print(f"Against B: {randomSample[1]['name']}, {randomSample[1]['description']}, {randomSample[1]['country']}")

userChoice = input("Who has more followers? Type 'A' or 'B': ").lower()

a_followers = randomSample[0]['follower_count']
b_followers = randomSample[1]['follower_count']


def print_result(choice_a, choice_b, user_choice, winner):
    if user_choice == winner.lower():
        print("You won!")
    else:
        print("You lose!")

    print(f"{choice_a['name']} has {choice_a['follower_count']} followers")
    print(f"{choice_b['name']} has {choice_b['follower_count']} followers")


# Determine  winner
if a_followers > b_followers:
    winner = "A"
else:
    winner = "B"

# call print function
print_result(randomSample[0], randomSample[1], userChoice, winner)
