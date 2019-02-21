# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab09 Loops2
# 20 Feb 2019

# Imports
import random

# Begin Average
# Prompt the user for the first score and initialize accumulator/index
new_score = int(input('Enter score: '))
score = 0
i = 0
while new_score >= 0 and new_score <= 100:
    score += new_score
    new_score = int(input('Enter score: '))
    i += 1

# Prevents a divide by zero error
if i == 0:
    i = 1

# Calculates and returns average
avg = score / i
print('Average score: ', avg, '%', sep='')
# End Average

# Begin Measurement Validation
# Prompts the user initially for measurement input
temp = float(input('Enter temperature: '))

# Checks the temperature and validates within range
while not (temp >= 94.0 and temp <= 107.0):
    print('Temperature is out of range.')
    temp = float(input('Enter temperature: '))

# When the temperature is within range, it prints the temperature
print('You entered', temp, 'degrees.')
# End Measurement Validation

# Begin random number guessing game
# Randomly generate a number between 1 and 1024 inclusive
random_num = random.randint(1, 1024)

# Tell the user what is about to happen
print('I\'m thinking of an integer between 1 and 1024 inclusive.\nSee if you can guess what it is!')

# Prompts the user to input their guess
guess = int(input('What is your guess? '))

# Counts the number of guesses
num_guesses = 1

# Checks the guess and continually tells the user if their too high or too low
# Breaks out of the loop when the user guesses the correct number
while guess != random_num:
    if guess < random_num:
        print('Your guess it too low.')
        guess = int(input('Guess again! '))
    elif guess > random_num:
        print('Your guess is too high.')
        guess = int(input('Guess again! '))
    num_guesses += 1

# If the user guesses the correct number, let them know
print('Your guess is exactly right! The number was ', random_num, '. It took you ', num_guesses, ' guesse(s).' , sep='')
# End random number guessing game
