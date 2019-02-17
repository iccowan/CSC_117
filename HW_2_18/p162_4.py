# Ian Cowan
# Feb 18 2019
# Problem 4 on page 162
# Distance Traveled

# Prompts the user to input the speed (in mph) and hours of travel
mph = int(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has the vehicle been traveling? '))

# Adds the headers to the table
print('')
print('Hour\tDistance Traveled')
print('-------------------------')

# Loops through each hour and prints the information for that hour
for hr in range(hours):
    hr = hr + 1
    distance = hr * mph
    print(str(hr) + '\t' + str(distance))
