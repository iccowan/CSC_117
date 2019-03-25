# Ian Cowan
# Mar 25 2019
# Problem 8 on page 335
# Name Search

# Define boyGirlNamesToLists()
# Inputs:
#   NONE
# Outputs:
#   list: boy
#   list: girl
def boyGirlNamesToLists():
    # Open BoyNames.txt
    file_in = open('BoyNames.txt', 'r')

    # Init variables
    boy = list()

    # Loop through each line of the boy names and add it to the list
    for name in file_in:
        boy.append(name.rstrip('\n'))

    # Close BoyNames.txt and open GirlNames.txt
    file_in.close()
    file_in = open('GirlNames.txt', 'r')

    # Init variables
    girl = list()

    # Loop through each line of the girl names and add it to the list
    for name in file_in:
        girl.append(name.rstrip('\n'))

    return boy, girl

# Define main()
def main():
    # Call boyGirlNamesToLists()
    boys, girls = boyGirlNamesToLists()

    # Prompt the user for a boy name and a girl name
    boy_name = input('Enter a boy name ("DONE" to quit): ')
    girl_name = input('Enter a girl name ("DONE" to quit): ')

    # Sentinel
    while boy_name != 'DONE' and girl_name != 'DONE':
        # Check to see if the boy name is in the list
        if boy_name in boys:
            print('The name', boy_name, 'is in the list of most common boy names!')
        elif (boy_name not in boys) and boy_name != '':
            print('The name', boy_name, 'is not in the list of most common boy names.')

        # check to see if the girl name is in the list
        if girl_name in girls:
            print('The name', girl_name, 'is in the list of most common girl names!')
        elif (girl_name not in girls) and girl_name != '':
            print('The name', girl_name, 'is not in the list of most common girl names.')

        # Prompt the user for a boy name and a girl name
        boy_name = input('Enter a boy name ("DONE" to quit): ')
        girl_name = input('Enter a girl name ("DONE" to quit): ')

# Call main()
main()
