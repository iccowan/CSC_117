# Ian Cowan
# Feb 18 2019
# Problem 12 on page 163
# Population Calculation

# Prompts the user to input the appropiate fields
start = int(input('Starting number of organisms: '))
daily_inc = float(input('Daily increase (percentage): '))
num_days = int(input('Number of days to multiply: '))

# Adds the headers to the table
print('Day\tApproximate Population')
print('-----------------------------')

# Sets the last_pop variable
last_pop = start
daily_inc = 1 + (daily_inc / 100)

# Loops through each day and calculates the estimated population and prints the result
for day in range(num_days):
    day = day + 1
    if day == 1:
        pop = float(start)
    else:
        pop = last_pop * daily_inc
    print(str(day) + '\t' + str('{:.3f}'.format(pop)))
    last_pop = pop
