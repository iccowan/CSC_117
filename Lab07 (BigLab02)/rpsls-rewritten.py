import random

def getThrows(gamemode):
    # Ask the user for their throw
    print('Choose your throw!')
    print('1 => Rock')
    print('2 => Paper')
    print('3 => Scissors')
    print('4 => Lizard')
    print('5 => Spock')
    user_t = input()

    if gamemode == 1:
        throw_2 = random.randint(1, 5)
    else:
        print('Player 2 choose your throw!')
        throw_2 = input()

    return user_t, throw_2

def printWinner(gamemode, winner):
    if winner == 0:
        print('It was a tie!')
    elif winner == 1:
        print('Player 1 won!')
    elif winner == 2:
        if gamemode == 1:
            print('The computer won!')
        else:
            print('Player 2 won!')

def main():
    # Find out how the user wants to play
    print('Would you like to play against the computer or against another person?')
    print('1 => Computer')
    print('2 => Another Person')
    gamemode = int(input())
    print(gamemode)

    # Get the 2 throws (user and user/computer)
    throw_1, throw_2 = getThrows(gamemode)

    # Get all of the winning combinations
    winning_combos = {'1-1' : 0, '1-2' : 2, '1-3' : 1, '1-4' : 1, '1-5' : 2, \
                      '2-1' : 1, '2-2' : 0, '2-3' : 2, '2-4' : 2, '2-5' : 2, \
                      '3-1' : 2, '3-2' : 1, '3-3' : 0, '3-4' : 1, '3-5' : 2, \
                      '4-1' : 2, '4-2' : 1, '4-3' : 2, '4-4' : 0, '4-5' : 2, \
                      '5-1' : 1, '5-2' : 1, '5-3' : 1, '5-4' : 1, '5-5' : 0}

    # Get the combo that we have
    combo = str(throw_1) + '-' + str(throw_2)
    print(combo)
    winner = winning_combos[combo]

    # Tell them who won!
    printWinner(gamemode, winner)

main()
