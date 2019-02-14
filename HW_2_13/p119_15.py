# Ian Cowan
# Feb 13 2019
# Problem 15 on page 119
# Time Calculator

# Prompts the user for a number of seconds
seconds = int(input('How many seconds would you like to convert? '))

# Checks to see the number of minutes or seconds or hours for the number of seconds the user inputted
if seconds < 60 and seconds >= 0:
    # Will only ever be seconds
    print('There are', seconds, 'seconds in', seconds, 'seconds.')
elif seconds < 3600 and seconds >= 60:
    # Will always be minutes and seconds
    print('There are', seconds // 60, 'minutes and', seconds % 60, 'seconds in', seconds, 'seconds.')
elif seconds < 86400 and seconds >= 3600:
    # Will always be hours, minutes, and seconds
    print('There are', seconds // 3600, 'hours,', (seconds % 3600) // 60, 'minutes, and', (seconds % 3600) % 60, 'seconds in', seconds, 'seconds.')
elif seconds >= 86400:
    # Will always be days, hours, minutes, seconds
    print('There are', seconds // 86400, 'days,', (seconds % 86400) // 3600, 'hours,', ((seconds % 86400) % 3600) // 60, 'minutes, and', ((seconds % 86400) % 3600) % 60, 'seconds in', seconds, 'seconds.')
else:
    # Error if the user inputs a negative time
    print('Error: That is not a valid time.')
