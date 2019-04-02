# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab20 Strings
# 01 Apr 2019

# Define initAcids()
# Inputs:
#   NONE
# Outputs:
#   NONE
def initAcids():
    # Create the global variable
    # acids FORMAT: [
    #               [str: triplet, str: acid]
    #               ]
    global acids
    acids = list()

    # Open the file
    f_in = open('standardcode.txt', 'r')

    # Loop through each line and add it to the list
    for line in f_in:
        line = line.strip()
        line_split = line.split(',')
        acids.append(line_split)

    # Close the file
    f_in.close()

# Define getDnaStrings()
# Inputs:
#   NONE
# Outputs:
#   str: m
#   str: p
def getDnaStrings():
    # Open the files
    fm_input = open('mouse.txt', 'r')
    fp_input = open('possum.txt', 'r')

    # Get the DNA strings and get rid of white space and make sure all uppercase
    m = fm_input.readline().strip().upper()
    p = fp_input.readline().strip().upper()

    # Close the files
    fm_input.close()
    fp_input.close()

    return m, p

# Define isValidDnaString()
# Inputs:
#   str: dna
# Outputs:
#   bool: is_valid
def isValidDnaString(dna):
    # Init variable, assume valid
    is_valid = True

    # Loop through each character and make sure it is T, A, C, or G
    for c in dna:
        if not(c == 'T' or c == 'A' or c == 'C' or c == 'G'):
            is_valid = False

    return is_valid

# Define keepGoing()
# Inputs:
#   bool: m_valid
#   bool: p_valid
# Outputs:
#   bool: both_valid
def keepGoing(m_valid, p_valid):
    # Init variable
    both_valid = False
    
    # Check to see if they are both valid    
    if not(m_valid) and not(p_valid):
        print('Uh, oh. The mouse and possum DNA strings are not valid.')
    elif not m_valid:
        print('Uh, oh. The mouse DNA string is not valid.')
    elif not p_valid:
        print('Uh, oh. The possum DNA string is not valid.')
    else:
        print('Both strings of DNA are valid.')
        
        # Update for this case only
        both_valid = True

    return both_valid

# Define compareDna()
# Inputs:
#   str: dna1
#   str: dna2
# Outputs:
#   int: diff
def compareDna(dna1, dna2):
    # Init variable
    i = 0
    diff = 0

    # Loop through each char in dna1 and compare it to dna2
    for c in dna1:
        if c != dna2[i]:
            diff += 1
        i += 1

    return diff

# Define printDnaAndComp()
# Inputs:
#   str: m
#   str: p
# Outputs:
#   NONE
def printDnaAndComp(m, p):
    # Get the comp's
    m_c = findDnaComp(m)
    p_c = findDnaComp(p)

    # Print everything as necessary
    print(m, 'mouse')
    print(m_c, 'mouse-complement')
    print(p, 'possum')
    print(p_c, 'possum-complement')

# Define findDnaComp()
# Inputs:
#   str: dna
# Outputs:
#   str: comp
def findDnaComp(dna):
    # Init variable
    comp = ''

    # Loop through each char and find compliment
    for char in dna:
        if char == 'T':
            comp += 'A'
        elif char == 'A':
            comp += 'T'
        elif char == 'G':
            comp += 'C'
        elif char == 'C':
            comp += 'G'

    return comp

# Define getTriplets()
# Inputs:
#   str: dna
# Outputs:
#   list: triplets
def getTriplets(dna):
    # Init variables
    trip = ''
    triplets = list()
    i = 1

    # Loop through each letter and if we have 3 letters, add it to the list
    for c in dna:
        trip += c

        # If we have 3, add it to the list
        if i % 3 == 0:
            triplets.append(trip)
            trip = ''

        # Update variable
        i += 1

    return triplets

# Define getAminoAcids()
# Inputs:
#   list: trip
# Outputs:
#   str: acids
def getAminoAcids(trip):
    # Init variables
    acids_for_trip = ''
    
    # Loop through each triplet and find the acid assigned to it
    for t in trip:
        acids_for_trip += getAcid(t)

    return acids_for_trip

# Define getAcid()
# Inputs:
#   str: triplet
# Outputs:
#   str: acid
def getAcid(triplet):
    # Loop through each triplet in the acids and find the acid
    for t in acids:
        if t[0] == triplet:
            acid = t[1]

    return acid

# Define main()
def main():
    # Call initAcids()
    initAcids()
    
    # Get mouse and possum DNA strings
    mouse, possum = getDnaStrings()

    # Check both strings to make sure they are valid strings of DNA
    m_valid = isValidDnaString(mouse)
    p_valid = isValidDnaString(possum)
    
    # Check to see if we keep going. If not, empty return to quit
    if not keepGoing(m_valid, p_valid):
        return
    
    # Continue if we keep going...
    # Call compareDna() and print the result
    dna_diff = compareDna(mouse, possum)

    print('Strands differ in ' + str(dna_diff) + ' place(s).')

    # Call printDnaAndComp()
    printDnaAndComp(mouse, possum)

    # Call getTriplets() for each DNA string
    m_trip = getTriplets(mouse)
    p_trip = getTriplets(possum)

    # Call getAminoAcids() for each triplet
    m_acids = getAminoAcids(m_trip)
    p_acids = getAminoAcids(p_trip)

    # Print the results
    print(m_acids + ' mouse')
    print(p_acids + ' possum')

# Call main()
main()
