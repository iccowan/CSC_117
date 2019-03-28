# Ian Cowan
# Mar 27 2019
# Problem 10 on page 336
# World Series Search

# Define importFileToList()
# Inputs:
#   str: file_name
# Outputs:
#   list: file_list
def importFileToList(file_name):
    # Open the file
    file_in = open(file_name, 'r')

    # Init variables
    file_list = list()

    # Loop through each line in the file putting it into the list
    for line in file_in:
        file_list.append(line.rstrip('\n'))

    # Close the file
    file_in.close()

    return file_list

# Define timesInList()
# Inputs:
#   str: item
#   list: search_list
# Outputs:
#   int: times_appear
def timesInList(item, search_list):
    # Init variables
    i = 0

    # Loop through the list and see the number of times item appears
    for j in search_list:
        if j == item:
            i += 1

    return i

# Define main()
def main():
    # Call importFileToList()
    world_series = importFileToList('WorldSeriesWinners.txt')

    # Prompt the user to search for a team
    team = input('Enter the name of a baseball team: ')

    # Check to see if the team is in the list
    # If they are call timesInList()
    # If they aren't print that info
    if team in world_series:
        times_won = timesInList(team, world_series)
        print('The team, ' + team + ' won the world series', times_won, 'times between 1903 and 2009!')
    else:
        print('The team, ' + team + ' did not win the world series between 1903 and 2009.')

# Call main()
main()
