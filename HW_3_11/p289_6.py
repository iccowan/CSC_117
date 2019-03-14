# Ian Cowan
# Mar 11 2019
# Problem 6 on page 289
# Average of Numbers

# Define averageNumInFile()
# Inputs:
#   file: file
# Outputs:
#   float: average
def averageNumInFile(file):
    # Initialize variables
    total = 0
    i = 0

    # Loop through each number in the file
    for num in file:
        # Add the number to the total
        total += float(num)

        # Update the index
        i += 1

    # Calculate the average if possible. If not return 0
    if i == 0:
        average = 0
    else:
        average = total / i

    return average

# Define main()
def main():
    # Open file_in
    file_in = open('numbers.txt', 'r')

    # Call averageNumInFile()
    avg = averageNumInFile(file_in)

    # Print the avergae of the numbers in the file
    print('The average of all the numbers in numbers.txt is', avg)

    # Close file_in
    file_in.close()

# Call main()
main()
