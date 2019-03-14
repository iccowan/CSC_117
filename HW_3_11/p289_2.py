# Ian Cowan
# Mar 11 2019
# Problem 2 on page 289
# File Head Display

# Define printFirstFiveLines()
# Inputs:
#   file: file
# Outputs:
#   NONE
def printFirstFiveLines(file):
    # Initialize variable
    i = 0
    line = file.readline().rstrip('\n')

    # Loops through the first 5 lines and print them
    # Terminates if the line returns an empty string or we reach 5 lines
    while i < 5 and line != '':
        print(line)

        # Update variables
        line = file.readline().rstrip('\n')
        i += 1

# Define main()
def main():
    # Prompt the user to input the filename
    file_name = input('What is the name of the file you want to read (include extension)? ')

    # Open file_in
    file_in = open(file_name, 'r')

    # Call printFirstFiveLines
    printFirstFiveLines(file_in)

    # Close file_in
    file_in.close()

# Call main()
main()
