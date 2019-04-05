# Ian Cowan
# Apr 3 2019
# Problem 3 on page 416
# File Encryption and Decryption

# Define loadEncryption()
# Inputs:
#   str: file_name
#   str: cryption
# Outputs:
#   dict: encryption
def loadEncryption(file_name, cryption):
    # Open the file
    file_in = open(file_name, 'r')

    # Init variables
    encryption = dict()

    # Read through each line, adding each value to the encryption table depending on type of cryption
    for line in file_in:
        line = line.strip()

        # Skip comment lines
        if line[0:1] != '#':
            if cryption == 'E':
                line = line.split(':')
                encryption[line[0]] = line[1]
            else:
                line = line.split(':')
                encryption[line[1]] = line[0]

    return encryption

# Define encryptDecrypt()
# Inputs:
#   str: file_name
#   dict: key
# Outputs:
#   NONE
def encryptDecrypt(file_name, key):
    # Open the files
    file_in = open(file_name, 'r')
    file_name = file_name.split('.')
    file_out = open(file_name[0] + '_crypted.txt', 'w')

    # Go through each line in the input file, encrypt it (or decrypt it) and copy it to output
    for line in file_in:
        line = line.strip()
        new_line = ''

        for char in line:
            if char == ' ' or char == '.' or char == ',' or char == '!' or char == '?' or \
               char == '-' or char == '"' or char == "'" or char == '/':
                new_line += char
            elif char in key:
                new_line += key[char]
            else:
                new_line += char

        file_out.write(new_line + '\n')

# Define main()
def main():
    # Prompt the user on whether they would like to encrypt or decrypt
    mode = input('Would you like to encrypt or decrypt? (E/D) ').upper()
    file_name = input('Enter file name to encrypt/decrypt: ')

    # Validation
    while mode != 'E' and mode != 'D':
        print('Invalid type. E or D.')
        mode = input('Would you like to encrypt or decrypt? (E/D) ').upper()

    # Load the encryption file
    encrypt_table = loadEncryption('ian_encryption_key.txt', mode)

    # Call encryptDecrypt()
    encryptDecrypt(file_name, encrypt_table)

# Call main()
main()
