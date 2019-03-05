# Ian Cowan
# Mar 04 2019
# Problem 10 on page 230
# Feet to Inches Conversion

# Define feetToInches()
# Inputs:
#   float: feet
# Outputs:
#   float: inches
def feetToInches(feet):
    # Conversion
    inches = feet * 12

    # Return the inches
    return inches

# Define main()
def main():
    # Prompt the user to input a number of feet
    feet = float(input('Feet: '))

    # Call feetToInches()
    inches = feetToInches(feet)

    # Return the number of inches
    print('Inches:', inches)

# Call main()
main()
