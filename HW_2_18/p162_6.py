# Ian Cowan
# Feb 18 2019
# Problem 6 on page 162
# Celsius to Fahrenheit Table

# Adds the headers to the table
print('Degrees Celcius\t\tDegrees Farenheit')
print('-----------------------------------------')

# Loops through 0 to 20 degrees C and converts to Farenheit
for deg_c in range(21):
    deg_f = ((9/5) * deg_c) + 32
    print(str(deg_c) + '\t\t\t' + str('{:.2f}'.format(deg_f)))
