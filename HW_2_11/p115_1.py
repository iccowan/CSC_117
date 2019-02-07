# Ian Cowan
# Feb 11 2019
# Problem 1 on page 115
# Day of the Week

# Prompts the user for a number 1 through 7
day = int(input('Enter a number 1 through 7 to see the corresponding day of the week! '))

# Sets the day of the week variable
if(day == 1):
    day_words = 'Monday'
elif(day == 2):
    day_words = 'Tuesday'
elif(day == 3):
    day_words = 'Wednesday'
elif(day == 4):
    day_words = 'Thursday'
elif(day == 5):
    day_words = 'Friday'
elif(day == 6):
    day_words = 'Saturday'
elif(day == 7):
    day_words = 'Sunday'
else:
    day_words = False

# Returns the day of the week OR errors if the value isn't allowed
if(day_words != False):
    print('The day of the week you chose is... ' + day_words + '!')
else:
    print('Error: You entered a value that is not allowed')
