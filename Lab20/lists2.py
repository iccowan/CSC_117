# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab20 Lists 2
# 27 Mar 2019

# Define readCapitals()
# Inputs:
#   NONE
# Outputs:
#   list: records
def readCapitals():
    # Open us-state-capitals.txt
    file_in = open('us-state-capitals.txt', 'r')

    # Init variables
    state = file_in.readline()
    records = list()

    # Loops through each record
    while state != '':
        # Skip sep lines
        if state != '\n':
            # Gets all information
            state = state.rstrip('\n')
            city = file_in.readline().rstrip('\n')
            lat = float(file_in.readline().rstrip('\n'))
            lon = float(file_in.readline().rstrip('\n'))

            # Create list
            rec = [state, city, lat, lon]

            # Add rec to records
            records.append(rec)

        # Get next state
        state = file_in.readline()

    # Close us-state-capitals.txt
    file_in.close()

    return records

# Define printTable()
# Inputs:
#   list: records
# Outputs:
#   NONE
def printTable(records):
    # Loop through each record
    for r in records:
        # Loop through each element of the record
        for i in r:
            # Add a specific number of tabs depending on length
            if len(str(i)) >= 8:
                print(i, end='\t')
            else:
                print(i, end='\t\t')
            
        # Line break
        print()

# Define southOfMasonDixon()
# Inputs:
#   list: records
# Outputs:
#   new_records
def southOfMasonDixon(records):
    # Init variables
    new_records = list()
    
    # Loop through each record
    for r in records:
        # Check the record to see if it is south of the MDL
        if r[2] < 39.7222:
            # For safety, make a copy
            n = list()
            for i in r:
                n.append(i)

            new_records.append(n)

    return new_records

# Define findLongitude()
# Inputs:
#   str: capital
#   list: all_capitals
# Outputs:
#   float: lon
def findLongitude(capital, all_capitals):
    # Init variables
    lon = None

    # Loop through each record and see if it is in all
    for r in all_capitals:
        if r[1] == capital and lon == None:
            lon = r[3]

    # Assigns lon 0.0 if it doesn't have one already
    if lon == None:
        lon = 0.0

    return lon

# Define westOf()
# Inputs:
#   str: capital
#   list: all_capitals
# Outputs:
#   list: capitals
def westOf(capital, all_capitals):
    # Get the longitude of the capitals
    lon = findLongitude(capital, all_capitals)

    # Init variables
    capitals = list()

    # Loop through and check longitudes
    for c in all_capitals:
        if c[3] < lon:
            # For safety, make a copy
            n = list()
            for i in c:
                n.append(i)

            # Add the record to capitals
            capitals.append(n)

    return capitals

# Define main()
def main():
    # Call readCapitals()
    records = readCapitals()

    # Call printTable()
    printTable(records)

    # Call southOfMasonDixon()
    southern = southOfMasonDixon(records)

    # Prompt user to enter a capital
    cap = input('Enter a capital: ')

    # Call westOf()
    caps_west = westOf(cap, records)

    # Create a break and a label:
    print()
    print('Capitals West of ' + cap + ':')

    # Call printTable()
    printTable(caps_west)

main()
