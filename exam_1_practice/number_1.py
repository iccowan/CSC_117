# Exam 1 Practice
# Question Number 1
# ft to cm

# Prompt the user for the conversion they want to do
print('What type of conversion would you like to do?')
print('1 = FEET to CENTIMETERS\n2 = CENTIMETERS TO FEET')
conversion = input('')

# Checks to make sure the user entered a correct value
while conversion != '1' and conversion != '2':
    print('Please enter a valid number (1 or 2)')
    conversion = input('')

# Converts conversion to class int
conversion = int(conversion)

# Converts depending on the user's selection
if conversion == 1:
    feet = float(input('How many feet would you like to convert to centimeters? '))
    while feet < 0:
        feet = float(input('Please enter a valid number of feet: '))
    cm = feet * 30.48

    # Returns the number of cm in ft
    print('There are', '{:.3f}'.format(cm), 'centimeters in', feet, 'feet!')
else:
    cm = float(input('How many centimeters would you like to convert to feet? '))
    while cm < 0:
        cm = float(input('Please enter a valid number of centimeters: '))
    feet = cm / 30.48

    # Returns the number of ft in cm
    print('There are', '{:.3f}'.format(feet), 'feet in', cm, 'centimeters!')
