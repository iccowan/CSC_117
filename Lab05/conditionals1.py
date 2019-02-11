# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab05 Conditionals 1
# 11 Feb 2019

# Import packages
import random

# Begin even or odd
# Prompts the user for a number to check
number = int(input('What number would you like to check for even/odd? '))

# Performs calculations
remain = number % 2

# Checks the remainder and returns a response
if remain == 1:
    print('The number,', number, 'is odd')
else:
    print('The number,', number, 'is even')
# End even or odd

# Begin coin flip
# Asks the user if they want to begin (no input required)
input('Ready to Flip a Coin? (Enter)')

# Randomly selects either 1 or 0
coin = random.randint(0, 1)

# Returns heads or tails based on the randomly generated number
if coin == 1:
    print('The coin has landed on... \nHeads!')
else:
    print('The coin has landed on... \nTails!')
# End coin flip

# Begin random integer game
# Randomly generates a number
number = random.randint(1, 4)

# Prompts the user for their guess
user_number = int(input('Guess the number. Hint: it\'s 1 through 4! '))

# Checks the user's guess with the random number and returns a response
if user_number > number:
    print('Your guess was too high!')
elif user_number < number:
    print('Your guess was too low!')
else:
    print('Your guess was right!')

# Returns the user's number and the randomly generated number
print('Your guess:', user_number)
print('Randomly generated number:', number)
# End random integer game

# Begin coin counter
# Prompts the user for the number of coins
penny = int(input('How many pennies do you have? '))
nickel = int(input('How many nickels do you have? '))
dime = int(input('How many dimes do you have? '))
quarter = int(input('How many quarters do you have? '))
half_dollar = int(input('How many half dollars do you have? '))

# Adds up the total change
total_change = (penny * 1) + (nickel * 5) + (dime * 10) + (quarter * 25) + (half_dollar * 50)

# Finds the amount of change left over that doesn't go into an even dollar
change_leftover = total_change % 100

# Checks to see if any change is left over, and returns a response
if change_leftover == 0:
    print('There is no leftover change')
else:
    print('You have', change_leftover, 'cents leftover')
# End coin counter
