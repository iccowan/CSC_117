# Ian Cowan
# Feb 13 2019
# Problem 9 on page 117
# Roulette Wheel

# Prompts the user to input a pocket number
pocket = int(input('What roulette wheel pocket number would you like to check? '))

# Checks the pocket number and determines whether it is red or black
if pocket >= 0 and pocket <= 36:
    if pocket == 0:
        print('Pocket 0 is green.')
    elif pocket >= 1 and pocket <= 10:
        if pocket % 2 == 0:
            print('Pocket', pocket, 'is black.')
        else:
            print('Pocket', pocket, 'is red.')
    elif pocket >= 11 and pocket <= 18:
        if pocket % 2 == 0:
            print('Pocket', pocket, 'is red.')
        else:
            print('Pocket', pocket, 'is black.')
    elif pocket >= 19 and pocket <= 28:
        if pocket % 2 == 0:
            print('Pocket', pocket, 'is black.')
        else:
            print('Pocket', pocket, 'is red.')
    elif pocket >= 29 and pocket <= 36:
        if pocket % 2 == 0:
            print('Pocket', pocket, 'is red.')
        else:
            print('Pocket', pocket, 'is black.')
else:
    # Errors for a number outside the allowed range
    print('Error: You must input a pocket number between 0 and 36')
