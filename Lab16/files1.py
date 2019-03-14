# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab16 File IO 1
# 11 Mar 2019

# Define step1()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step1():
    # Open people.txt for writing
    file_out = open('people.txt', 'w')
    
    # Prompt the user for the first name
    name = input('Enter name ("DONE" to finish): ')

    # Loop until the name is DONE
    while name != 'DONE':
        # Makes sure there is actually a name (Assumes a blank space is a mistake)
        if name != '':
            # Add the name to the file
            file_out.write(name + '\n')
        
        # Ask the user for the next name
        name = input('Enter name ("DONE" to finish): ')

    # Close file_out
    file_out.close()

# Define step2()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step2():
    # Open the file we created in step 1
    file_in = open('people.txt', 'r')

    # Print each name onto the console
    for name in file_in:
        print(name, end='')

    # Close file_in
    file_in.close()

# Define copyFile() (step3)
# Inputs:
#   NONE
# Outputs:
#   NONE
def copyFile():
    # Ask the user for the file name
    file_name = input('Enter the new file name to copy names to (exclude extension): ')
    
    # Open the file we created in step 1 and a new file
    file_in = open('people.txt', 'r')
    file_out = open(file_name + '.txt', 'w')

    # For each line in file_in, copy the information to file_out
    for line in file_in:
        file_out.write(line)

    # Close file_in & file_out
    file_in.close()
    file_out.close()

# Define main()
def main():
    # Call step1()
    step1()

    # Call step2()
    step2()

    # Call copyFile()
    copyFile()

# Call main()
main()
