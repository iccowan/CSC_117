# Ian Cowan
# Lab Partner: Josh West
# CSC 117b BigLab07 Crack Code
# 5 Apr 2019
# Help Sonic Crack the Code!

# Import Packages
import random
import time

# Define getWords()
# Inputs:
#   NONE
# Outputs:
#   list: all_words
def getWords():
    # Open the wordlist
    file_in = open('wordlist.txt', 'r')

    # Init variables
    all_words = list()

    # Loop through each line and append it to the
    for line in file_in:
        line = line.strip().upper()
        all_words.append(line)

    return all_words

# Define printInstructions()
# Inputs:
#   NONE
# Outputs:
#   NONE
def printInstructions():
    print('Help Sonic save the day by cracking the secret passphrase')
    print('to gain access to the servers of the evil Doctor Eggman!')
    print('The passphrase consists of three randomly selected words.')
    print('You can guess as many letters as you like.  However, you')
    print('are allowed only 6 incorrect guesses.  After that, you will')
    print('lose the game and the server will be locked forever (until')
    print('the next round, that is!).  Let\'s play!  Here is your clue:')

# Define playGame()
# Inputs:
#   list: all_words
# Outputs:
#   NONE
def playGame(all_words):
    # Length of all_words
    total_words = len(all_words)

    # Play until the user wants to stop
    gameOver = False
    while not gameOver:
    
        # Choose 3 random words
        word1_i = random.randint(0, total_words - 1)
        word2_i = random.randint(0, total_words - 1)
        word3_i = random.randint(0, total_words - 1)

        # Make sure none of the words are repeating
        word_is = uniqueIndex(word1_i, word2_i, word3_i, total_words)

        # Get the words associated with the three indexes
        words = list()
        for i in word_is:
            words.append(all_words[i])

        # At last, play the game!
        win = playWordGame(words)

        # Print something depending on whether the user won or lost
        if win:
            print('Congratulations, you won!')
        else:
            print('Unfortunately, you lost. But let\'s play again!')

        # Finally, check and see if the user wants to play again
        play_again = input('Would you like to play again? [y/n] ').upper()

        if play_again == 'N':
            gameOver = True
        
# Define uniqueIndex()
# Inputs:
#   int: i1
#   int: i2
#   int: i3
#   int: total
# Outputs:
#   int: i1
#   int: i2
#   int: i3
def uniqueIndex(i1, i2, i3, total):
    # Check and make sure i1 and i2 are not the same
    while i1 == i2 or i2 == i3 or i1 == i3:
        i1 = random.randint(0, total - 1)
        i2 = random.randint(0, total - 1)
        i3 = random.randint(0, total - 1)

    return [i1, i2, i3]

# Define playWordGame()
# Inputs:
#   list: words
# Outputs:
#   bool: win
def playWordGame(words):
    # Call initVarForGame()
    unique_char, chars, incor_guess, current_correct, alphabet, alphabet_i = initVarForGame(words)
    
    # Play until the user either guesses the word or runs out of incorrect guesses
    while unique_char > 0 and incor_guess > 0:
        # Print out the current standing
        printStanding(current_correct, alphabet, incor_guess, unique_char)

        # Get the user's guess
        print(words)
        g = input('Guess a letter: ').upper()

        # Check and make sure the letter has not been guessed yet
        while g not in alphabet:
            print('Whoops, you\'ve already tried that letter!')
            g = input('Guess a letter: ').upper()

        # Update variables accordingly
        if g in chars:
            unique_char -= 1
            i = 0
            for w in words:
                j = 0
                for c in w:
                    if c == g:
                        k = 0
                        n_word = ''
                        for l in current_correct[i]:
                            if l != ' ':
                                if k == j:
                                    n_word += g + ' '
                                elif l.isalnum():
                                    n_word += l + ' '
                                else:
                                    n_word += '_ '
                                k += 1
                                
                        n_word = n_word.strip()
                        current_correct[i] = n_word

                    j += 1
                i += 1
        else:
            incor_guess -= 1
            print('Sorry,', g, 'does not appear occur in the passphrase.')

        # Remove the character from available characters
        alphabet[alphabet_i[g]] = ' '
        
    # Print final results
    printStanding(current_correct, alphabet, incor_guess, unique_char)

    # Determine whether they won or lost
    if incor_guess == 0:
        win = False
    else:
        win = True
        
    return win

# Define initVarForGame()
# Inputs:
#   list: words
# Outputs:
#   int: unique_char
#   list: chars
#   int: incor_guess
#   list: current_correct
#   list: alphabet
#   dict: alphabet_i
def initVarForGame(words):
    # Decide how many unique characters exist
    unique_char = 0
    chars = list()
    for w in words:
        for c in w:
            if c not in chars:
                chars.append(c)
                unique_char += 1

    # Init incorrect guesses
    incor_guess = 7

    # Make a list with all of the blanks for the words
    current_correct = list()
    for w in words:
        b = ''
        for char in w:
            b += '_ '

        b = b.strip()
        current_correct.append(b)
        
    # Make a list of the alphabet and a dictionary with the indexes of all letters
    alphabet = list()
    alphabet_i = dict()
    for ltr in range(65, 91):
        alphabet.append(chr(ltr))

    i = 0
    for j in alphabet:
        alphabet_i[j] = i
        i += 1

    return unique_char, chars, incor_guess, current_correct, alphabet, alphabet_i

# Define printStanding()
# Inputs:
#   list: current_correct
#   list: alphabet
#   int: incor_guess
#   int: unique_char
# Outputs:
#   NONE
def printStanding(current_correct, alphabet, incor_guess, unique_char):
    # Print out the current standing
    print()
    print('Passphrase:', end=' ')
    for j in current_correct:
        print(j, end='  ')
        time.sleep(0.05)
    print()
        
    print('Letters Available:', end=' ')
    for k in alphabet:
        print(k, end=' ')
        time.sleep(0.05)
    print()

    print('You have', incor_guess, 'incorrect guesse(s) remaining.')
    print('There are', unique_char, 'unique character(s) remaining.')

# Define main()
def main():
    # Call getWords()
    all_words = getWords()

    # Call printInstructions()
    printInstructions()
    
    # Call playGame()
    playGame(all_words)

# Call main()
main()
