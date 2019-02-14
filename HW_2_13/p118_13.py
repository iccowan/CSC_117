# Ian Cowan
# Feb 13 2019
# Problem 13 on page 118
# Shipping Charges

# Prompts the user to enter the wait of a package
weight = float(input('What is the weight of the package? '))

# Determines the shipping cost of the package based on weight
if weight <= 2 and  weight >= 0:
    print('Shipping charges: $1.50')
elif weight > 2 and weight <= 6:
    print('Shipping charges: $3.00')
elif weight > 6 and weight <= 10:
    print('Shipping charges: $4.00')
elif weight > 10:
    print('Shipping charges: $4.75')
else:
    # Errors for a negative number
    print('Error: The weight you entered is not valid')
