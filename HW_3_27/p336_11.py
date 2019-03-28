# Ian Cowan
# Mar 27 2019
# Problem 11 on page 336
# Lo Shu Magic Square

# Define getNumbers()
# Inputs:
#   NONE
# Outputs:
#   list: numbers
def getNumbers():
    # Prompt the user for 3 sets of numbers for each row
    print('Enter 9 numbers total, between 1 and 9.')
    print('Enter the 3 numbers in left to right order for the row specified.')

    # Init variables
    row1 = list()
    row2 = list()
    row3 = list()

    # Loop 3 x 3 times and get 9 numbers total
    for i in range(1, 4):
        print('Column ' + str(i) + ': ')

        for j in range(1, 4):
            n = int(input('Enter the number for position ' + str(j) + ': '))

            # Validation
            while n <= 0 or n > 9:
                print('The number must be between 1 and 9.')
                n = int(input('Enter the number for position ' + str(j) + ': '))

            # Add the number to the appropiate list
            if i == 1:
                row1.append(n)
            elif i == 2:
                row2.append(n)
            elif i == 3:
                row3.append(n)

    # Put all lists together
    numbers = [row1, row2, row3]

    return numbers

# Define checkForMagic()
# Inputs:
#   list: numbers
# Outputs:
#   bool: magic
def checkForMagic(numbers):
    # Check the sum of the rows and columns and diagonals
    sum_row1 = 0
    for i in numbers[0]:
        sum_row1 += i

    sum_row2 = 0
    for i in numbers[1]:
        sum_row2 += i

    sum_row3 = 0
    for i in numbers[2]:
        sum_row3 += i

    sum_col1 = numbers[0][0] + numbers[1][0] + numbers[2][0]
    sum_col2 = numbers[0][1] + numbers[1][1] + numbers[2][1]
    sum_col3 = numbers[0][2] + numbers[1][2] + numbers[2][2]

    sum_diag1 = numbers[0][0] + numbers[1][1] + numbers[2][2]
    sum_diag2 = numbers[0][2] + numbers[1][1] + numbers[2][0]

    # Check to see if all of the sums are the same
    if (sum_row1 == sum_row2 and sum_row2 == sum_row3) and \
       (sum_row3 == sum_col1 and sum_col1 == sum_col2) and \
       (sum_col2 == sum_col3 and sum_col3 == sum_diag1) and \
       (sum_diag1 == sum_diag2 and sum_diag2 == sum_col1):
        magic = True
    else:
        magic = False

    return magic

# Define main()
def main():
    # Call getNumbers()
    numbers = getNumbers()

    # Call checkForMagic()
    magic = checkForMagic(numbers)

    # Show the user the numbers checked in a pretty box
    print()
    print('Your numbers to check:')
    print('-------------')
    for i in numbers:
        print('| ' + str(i[0]) + ' | ' + str(i[1]) + ' | ' + str(i[2]) + ' |')
        print('-------------')
    print()

    # Print a result depending on whether they work or not
    if magic:
        print('Those numbers work for a Lo Shu Magic Square!')
    else:
        print('Those numbers do not work for a Lo Shu Magic Square.')

# Call main()
main()
