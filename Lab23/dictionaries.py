# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab23 Dictionaries
# 03 Apr 2019

# Define getMisspel()
# Inputs:
#   NONE
# Outputs:
#   dict: misspells
def getMisspel():
    # Open misspellings.txt
    file_in = open('misspellings.txt', 'r')

    # Init variables
    misspells = dict()

    # Loop through each line and add to dictionary
    for line in file_in:
        words = line.strip().split(':')
        misspells[words[0]] = words[1]
    
    # Close file_in
    file_in.close()

    return misspells

# Define spellCheck()
# Inputs:
#   file: f
#   dict: misspells
# Outputs:
#   NONE
def spellCheck(f, misspells):
    # Get the first line to check
    f_line = f.readline().strip()
    
    # Split up the line to check
    words = f_line.split()

    # Open the file to write to
    file_out = open('fixed.txt', 'w')

    # Loop through each word and check to see if it is correct
    # If so, add it to the new file
    # If not, fix it and add it to the new file
    for w in words:
        if w in misspells:
            word_to_add = misspells[w]
        else:
            word_to_add = w

        word_to_add = removePunct(word_to_add)
        file_out.write(word_to_add + ' ')

    # Close file_out
    file_out.close()

# Define removePunct()
# Inputs:
#   str: word
# Outputs:
#   str: word_wo_p
def removePunct(word):
    # Init variables
    word_wo_p = ''

    # Loop through each character and check if it's punctuation
    for char in word:
        if char.isalnum():
            word_wo_p += char

    return word_wo_p

# Define wordCount()
# Inputs:
#   file: f
# Outputs:
#   dict: word_count
def wordCount(f):
    # Get the first line in file
    f_line = f.readline().strip()

    # Get each word in the line
    words = f_line.split()

    # Init variables
    word_count = dict()

    # Loop through each word
    # If it has already been counted, add 1 to its counter
    # If it is not in the dict, add it
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    return word_count

# Define printWordCount()
# Inputs:
#   dict: word_counts
# Outputs:
#   NONE
def printWordCount(word_counts):
    # Turn the dictionary into a list
    wc_list = list(word_counts.items())
    wc_list.sort()

    # Print all of the items in the list in the appropiate format
    for i in wc_list:
        print(i[0] + ':' + str(i[1]))

# Define main()
def main():
    # Call getMisspel()
    misspells = getMisspel()

    # Open the file to spell check
    file_in = open('checkme.txt', 'r')

    # Call spellCheck()
    spellCheck(file_in, misspells)

    # Close the file_in and reopen fixed.txt
    file_in.close()
    file_in = open('fixed.txt', 'r')

    # Call wordCount()
    word_count = wordCount(file_in)

    # Close file_in
    file_in.close()

    # Call printWordCount()
    printWordCount(word_count)

# Call main()
main()
