# Ian Cowan
# Mar 11 2019
# Problem 4 on page 289
# Item Counter

# Define countNamesInFile()
# Inputs:
#   file: file
# Outputs:
#   int: num_names
def countNamesInFile(file):
    # Initialize variables
    num_names = 0

    # Loop through each line and count
    for name in file:
        num_names += 1

    return num_names

# Define main()
def main():
    # Open file_in
    file_in = open('names.txt', 'r')

    # Call countNamesInFile()
    names = countNamesInFile(file_in)

    # Print the number of names
    print('There is a total of', names, 'names in names.txt!')

    # Close file_in
    file_in.close()

# Call main()
main()
