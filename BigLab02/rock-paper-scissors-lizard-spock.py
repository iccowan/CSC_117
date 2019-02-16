# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab01 Rock-Paper-Scissors-Lizard-Spock
# 21 Feb 2019

# Import Packages
import random

# Begin Rock-Paper-Scissors-Lizard-Spock
# Prompt the user for human vs. computer or computer vs. computer
print('Would you like to play against the computer or have the computer play against the computer?')
print('1 = Human vs. Computer', '2 = Computer vs. Computer', sep='\n')
gamemode = input('')

# Checks the gamemode and sets the throw one variable
# Makes sure the user inputed an allowed number
if gamemode == '1' or gamemode == '2':
    gamemode = int(gamemode)
    if gamemode == 1:
        # Human vs. Computer
        # Prompts the user for their choice for throw one
        print('What do you choose?')
        print('1 = Rock', '2 = Paper', '3 = Scissors', '4 = Lizard', '5 = Spock', sep='\n')
        throw_one = input('')
        if throw_one == '1' or throw_one == '2' or throw_one == '3' or throw_one == '4' or throw_one == '5':
            # Turns throw one into an integer if the user enters an appropiate value
            throw_one = int(throw_one)
        else:
            # Scolds the user and chooses a random choice for the user
            print('You did not enter a valid number, so we will randomly assign you an option.')
            thow_one = random.randint(1, 5)
    elif gamemode == 2:
        # Computer vs. Computer
        # Decides the choice the computer wants for throw one
        throw_one = random.randint(1, 5)
else:
    # If the user doesn't enter a valid number, it will scold then run as computer vs. computer
    print('You did not enter a valid number, so we will assume you want computer vs. computer.')
    throw_one = random.randint(1, 5)

# Randomly generates throw two
throw_two = random.randint(1, 5)

# Checks to see who wins and sets the winner as 'one' or 'two'
if throw_one == 3 and throw_two == 2:
    # Scissors cuts Paper (throw_one wins)
    winner = 1
    reason_of_win = 'Scissors cuts Paper'
elif throw_one == 2 and throw_two == 3:
    # Scissors cuts Paper (throw_two wins)
    winner = 2
    reason_of_win = 'Scissors cuts Paper'
elif throw_one == 2 and throw_two == 1:
    # Paper covers Rock (throw_one wins)
    winner = 1
    reason_of_win = 'Paper covers Rock'
elif throw_one == 1 and throw_two == 2:
    # Paper covers Rock (throw_two wins)
    winner = 2
    reason_of_win = 'Paper covers Rock'
elif throw_one == 1 and throw_two == 4:
    # Rock crushes Lizard (throw_one wins)
    winner = 1
    reason_of_win = 'Rock crushes Lizard'
elif throw_one == 4 and throw_two == 1:
    # Rock crushes Lizard (throw_two wins)
    winner = 2
    reason_of_win = 'Rock crushes Lizard'
elif throw_one == 4 and throw_two == 5:
    # Lizard poisons Spock (throw_one wins)
    winner = 1
    reason_of_win = 'Lizard poisons Spock'
elif throw_one == 5 and throw_two == 4:
    # Lizard poisons Spock (throw_two wins)
    winner = 2
    reason_of_win = 'Lizard poisons Spock'
elif throw_one == 5 and throw_two == 3:
    # Spock smashes Scissors (throw_one wins)
    winner = 1
    reason_of_win = 'Spock smashes Scissors'
elif throw_one == 3 and throw_two == 5:
    # Spock smashes Scissors (throw_two wins)
    winner = 2
    reason_of_win = 'Spock smahes Scissors'
elif throw_one == 3 and throw_two == 4:
    # Scissors decapitates Lizard (throw_one wins)
    winner = 1
    reason_of_win = 'Scissors decapitates Lizard'
elif throw_one == 4 and throw_two == 3:
    # Scissors decapitates Lizard (throw_two wins)
    winner = 2
    reason_of_win = 'Scissors decapitates Lizard'
elif throw_one == 4 and throw_two == 2:
    # Lizard eats Paper (throw_one wins)
    winner = 1
    reason_of_win = 'Lizard eats Paper'
elif throw_one == 2 and throw_two == 4:
    # Lizard eats Paper (throw_two wins)
    winner = 2
    reason_of_win = 'Lizard eats Paper'
elif throw_one == 2 and throw_two == 5:
    # Paper disproves Spock (throw_one wins)
    winner = 1
    reason_of_win = 'Paper disproves Spock'
elif throw_one == 5 and throw_two == 2:
    # Paper disproves Spock (throw_two wins)
    winner = 2
    reason_of_win = 'Paper disproves Spock'
elif throw_one == 5 and throw_two == 1:
    # Spock vaporizes Rock (throw_one wins)
    winner = 1
    reason_of_win = 'Spock vaporizes Rock'
elif throw_one == 1 and throw_two == 5:
    # Spock vaporizes Rock (throw_two wins)
    winner = 2
    reason_of_win = 'Spock vaporizes Rock'
elif throw_one == 1 and throw_two == 3:
    # As it always has, Rock crushes Scissors (throw_one wins)
    winner = 1
    reason_of_win = 'as it always has, Rock crushes Scissors'
elif throw_one == 3 and throw_two == 1:
    # As it always has, Rock crushes Scissors (throw_two wins)
    winner = 2
    reason_of_win = 'As it always has, Rock crushes Scissors'
else:
    # It's a Tie! (neither win)
    winner = 3
    reason_of_win = 'It was a tie'

# Tells the user the computer is working!
print('Rock ... Paper ... Scissors ... Lizard ... Spock ... Shoot! \n')

# Returns the winner and why the winner won
if gamemode == 1:
    if winner == 1:
        print('Congratulations, you beat the computer because ', reason_of_win, '!', sep='')
    elif winner == 2:
        print('Unfortunately, the computer beat you because ', reason_of_win, '.', sep='')
    elif winner == 3:
        print('You tied with the computer!')
else:
    if winner == 1:
        print('Player 1 beat Player 2 because ', reason_of_win, '!', sep='')
    elif winner == 2:
        print('Player 2 beat Player 1 because ', reason_of_win, '.', sep='')
    elif winner == 3:
        print('Player 1 and Player 2 tied!')
