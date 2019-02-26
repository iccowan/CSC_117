# Exam 1 Practice
# Question Number 3
# Bob/Alice Coin Flipping

# Import Packages
import random

# Initialize Variables
bob_wins = 0
alice_wins = 0

# Runs 1000 times
for i in range(1000):
    # Initialize Variables
    gameOver = False

    # Loops until gameOver is true
    while gameOver == False:
        # Bob's Turn
        # Generates a random number 1-1000
        coin_flip_bob = random.randint(1, 1000)

        # Heads up 6:4 advantage so 1-
        if 1 <= coin_flip_bob and 600 >= coin_flip_bob:
            bob_side = 1
            gameOver = True
        else:
            bob_side = 2

        # Alice's Turn if the game is not over
        if gameOver == False:
            # Generates a random number 1-1000
            coin_flip_alice = random.randint(1, 1000)

            # Heads up 6:4 advantage so 1-
            if 1 <= coin_flip_alice and 600 >= coin_flip_alice:
                alice_side = 1
                gameOver = True
            else:
                alice_side = 2

        # If either player won, add a win to the player's total
        if bob_side == 1:
            bob_wins += 1
        elif alice_side == 1:
            alice_wins += 1

# Return the number of times each player won at the end
print('Bob won a total number of', bob_wins, 'times.')
print('Alice won a total number of', alice_wins, 'times.')
