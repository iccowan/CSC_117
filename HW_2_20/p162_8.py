# Ian Cowan
# Feb 20 2019
# Problem 8 on page 162
# Sum of Numbers

# Prompts the user to enter numbers
# Sets index i to 0 and new_num to 0
i = 0
new_num = 0
# Creates the empty list, numbers
numbers = list()
# Loops until the user enters a negative number
while new_num >= 0:
    # Prompts the user for new_num
    new_num = int(input('Enter a positive number to add (negative number to calculate): '))
    # Checks for a positive integer
    if new_num > 0:
        # Inserts new_num into the list with index i
        numbers.append(new_num)
        
        i += 1

# Adds all of the numbers in the numbers list together and returns the result
total = 0
for num in numbers:
    total = total + num
print('The total of the numbers you inputted is: ', total, '!', sep='')
