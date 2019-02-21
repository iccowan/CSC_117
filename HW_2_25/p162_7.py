# Ian Cowan
# Feb 25 2019
# Problem 7 on page 162
# Pennies for Pay

# Prompts the user for the number of days
days = int(input('How many days would you like to calculate a penny salary for? '))

# Initialize variable
total_p = 0
earned = 1

# Adds the headers to the table
print('Day\tTotal Dollars')
print('---------------------')

# Foreach day, add some to pennies total
for day in range(1, days + 1):
    if day == 1:
        total_p = 1
    else:
        earned = 2 ** day
        total_p += earned

    # Turns pennies into dollars!
    total_d = total_p / 100

    # Returns the number of dollars in the table
    print(day, '$' + str('{:3,.2f}'.format(total_d)), sep='\t')
