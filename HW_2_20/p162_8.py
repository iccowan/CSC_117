# Ian Cowan
# Feb 20 2019
# Problem 8 on page 162
# Sum of Numbers

# Prompts the user to enter a new_num
new_num = int(input('Enter a positive integer to add (negative number to calculate): '))
# Initializes total accumulator
total = 0

# Loops until the user enters a negative number
while new_num >= 0:
    # Updates the accumulator variable
    total += new_num
    # Prompts the user for new_num
    new_num = int(input('Enter a positive integer to add (negative number to calculate): '))

# Returns the user's total
print('The total of the numbers you inputted is: ', total, '!', sep='')
