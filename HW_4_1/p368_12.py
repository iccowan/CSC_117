# Ian Cowan
# Apr 1 2019
# Problem 12 on page 368
# Pig Latin Translator

# Define convertToPig()
# Inputs:
#   str: eng
# Outputs:
#   str: pig
def convertToPig(eng):
    # Split up the words, init variables
    words = eng.split()
    pig = list()

    # Loop through each word and convert it to pig latin
    for w in words:
        # Move the last letter to the beginning
        new_word = w[1:]
        new_word = new_word + w[0] + 'AY'

        # Add "AY" to the end of the word
        pig.append(new_word)

    return ' '.join(pig)

# Define main()
def main():
    # Prompt the user for an English input, make all caps for consitency
    english = input('Enter the English phrase: ').upper()

    # Call convertToPig()
    pig_latin = convertToPig(english)

    # Print the English and Pig Latin
    print('English:', english)
    print('Pig Latin:', pig_latin)

main()
