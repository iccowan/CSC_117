# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab03 Conversions
# 06 Feb 2019

# Start USD to Euro conversion
# Prompts the user to enter USD
us_d = float(input('Enter the number of US dollars to convert to Euros '))

# Converts the USD to Euros
euro = format(us_d * 0.81)

# Returns the number of Euros
print('$' + str(us_d) + ' in Euros is €' + str(euro))
# End USD to Euro conversion

# Start lbs to kg conversion
# Prompts the user for pounds to convert to kilograms
lbs = float(input('How many pounds would you like to convert to kilograms? '))

# Converts lbs to kg
kgs = lbs * 0.453

# Returns the kilograms
print(str(lbs) + ' lbs in kilograms is ' + str(kgs) + ' kg')
# End lbs to kg conversion

# Start kg to lbs conversion
# Prompts the user for kilograms to convert to pounds
kgs = float(input('How many kilograms would you like to convert to pounds? '))

# Converts kg to lbs
lbs = kgs / 0.453

# Returns the pounds
print(str(kgs) + ' kg in pounds is ' + str(lbs) + ' lbs')
# End kg to lbs conversion

# Begin dividing
# Prompts the user to input the dividend and divisor
divid = float(input('Enter a number to divide (dividend) '))
div = float(input('Enter a number to divide the first number by (the divisor) '))

# Does the calculation to get the float and modulus
div_float = divid / div
div_mod = divid % div

# Returns the two calculations
print(str(divid) + ' divided by ' + str(div) + ' is ' + str(div_float))
print('The remainder of ' + str(divid) + ' divided by ' + str(div) + ' is ' + str(div_mod))
# End dividing
