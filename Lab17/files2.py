# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab16 File IO 2
# 13 Mar 2019

# Define readDonors()
# Inputs:
#   NONE
# Outputs:
#   str: file_name
def readDonors():
    # Call getFile()
    file_in, file_name = getFile()

    if file_in == None and file_name == None:
        return None

    # Loop through each record and print the information
    name = file_in.readline()
    while name != '':
        amount = file_in.readline()

        # Remove extra newline
        name = name.rstrip('\n')
        amount = amount.rstrip('\n')

        print('Name: ' + name, 'Amount: ' + amount, sep='\n')

        # Update name
        name = file_in.readline()

    # Close the file
    file_in.close()

    return file_name

# Define getFile()
# Inputs:
#   NONE
# Outputs:
#   file: file_in
def getFile():
    # Init variable
    file_exist = True

    # Ask for the file name
    file_name = input('What is the name of the file with the list of donors? ')

    # Attempt to open the file
    try:
        open(file_name, 'r')
    except FileNotFoundError:
        file_exist = False

    # Keep asking for the file name until it exists
    while (not (file_exist)) and file_name != 'QUIT':
        print('That file does not exist. Please enter a valid filename')
        # Ask for the file name
        file_name = input('What is the name of the file with the list of donors ("QUIT" to cancel)? ')

        # Attempt to open the file
        try:
            open(file_name, 'r')
            file_exist = True
        except FileNotFoundError:
            file_exist = False

    if file_name == 'QUIT':
        return None, None
    else:
        file = open(file_name, 'r')

    return file, file_name

# Define copyDonorsToSwap()
# Inputs:
#   str: file_name
# Outputs:
#   NONE
def copyDonorsToSwap(file_name):
    # Open donors.txt(r) and swap.txt(w)
    file_in = open(file_name, 'r')
    file_out = open('swap.txt', 'w')

    # Copy data from donors to swap
    # Call copyData()
    copyData(file_in, file_out)

    # Close donors.txt and swap.txt
    file_in.close()
    file_out.close()

# Define copyData()
# Inputs:
#   file: orig
#   file: copy
# Outputs:
#   NONE
def copyData(orig, copy):
    # Loops through each record
    name = orig.readline()
    while name != '':
        # Get the amount and strip
        amount = orig.readline().rstrip('\n')
        name = name.rstrip('\n')

        # Check to see if the user wants to delete the record
        delete = input('Would you like to delete ' + name + '? (y/n) ' )

        # Input validation
        while delete != 'y' and delete != 'n':
            print('Please enter either "y" or "n"')
            delete = input('Would you like to delete ' + name + '? (y/n) ' )

        # Only run if the user doesn't want to remove the user
        if delete == 'n':
            # Check to see if the user wants to update the record
            update = input('Would you like to update ' + name + '? (y/n) ')

            # Input validation
            while update != 'y' and update != 'n':
                print('Please enter either "y" or "n"')
                update = input('Would you like to update ' + name + '? (y/n) ')

            # Checks if the user wants to update the user
            if update == 'y':
                n_name = input('Enter the new name (blank for unchanged): ')
                n_amount = input('Enter the new donation amount (blank for unchanged): $')
            else:
                n_name = ''
                n_amount = ''

            # Checks for empty string
            if n_name != '':
                name = n_name
            if n_amount != '':
                amount = n_amount

            # Writes the new data in the copy file
            copy.write(name + '\n')
            copy.write(amount + '\n')

        # Update name
        name = orig.readline()

# Define copySwapToDonors()
# Inputs:
#   NONEcopyDonorsToSwap()
# Outputs:
#   NONE
def copySwapToDonors():
    # Open swap.txt and donors.txt
    file_in = open('swap.txt', 'r')
    file_out = open('donors.txt', 'w')

    # Copy each line in file_in to file_out
    for line in file_in:
        file_out.write(line)

# Define main()
def main():
    # Call readDonors()
    donors = readDonors()

    if donors != None:
        # Call copyDonorsToSwap()
        copyDonorsToSwap(donors)

        # Call copySwapToDonors()
        copySwapToDonors()
    else:
        print('Successfully cancelled.')

# Call main()
main()
