# Ian Cowan
# Apr 1 2019
# Problem 5 on page 367
# Alphabetic Phone Number Translator

# Define getNumPhoneNumber()
# Inputs:
#   str: pn
# Outputs:
#   str: pn_nums
def getNumPhoneNumber(pn):
    # Init variables
    pn_nums = ''

    # Loop through each character in pn and continue as appropiate
    for char in pn:
        if char == '-':
            pn_nums += '-'
        elif char.isdigit():
            pn_nums += char
        else:
            pn_nums += letterToNum(char)

    return pn_nums

# Define letterToNum()
# Inputs:
#   str: character
# Outputs:
#   str: number
def letterToNum(character):
    # Check the case that the letter fits
    if character == 'A' or character == 'B' or character == 'C':
        number = 2
    elif character == 'D' or character == 'E' or character == 'F':
        number = 3
    elif character == 'G' or character == 'H' or character == 'I':
        number = 4
    elif character == 'J' or character == 'K' or character == 'L':
        number = 5
    elif character == 'M' or character == 'N' or character == 'O':
        number = 6
    elif character == 'P' or character == 'Q' or character == 'R' or character == 'S':
        number = 7
    elif character == 'T' or character == 'U' or character == 'V':
        number = 8
    elif character == 'W' or character == 'X' or character == 'Y' or character == 'Z':
        number == 9

    return str(number)

# Define main()
def main():
    # Prompt the user to enter an alphanumeric phone number, convert to uppercase
    phone_number = input('Enter an alphanumeric phone number in the form XXX-XXX-XXXX: ').upper()

    # Call getNumPhoneNumber()
    num_phone_number = getNumPhoneNumber(phone_number)

    # Print the new number
    print('The phone number, ' + phone_number + ' is the representation of ' + num_phone_number)

# Call main()
main()
