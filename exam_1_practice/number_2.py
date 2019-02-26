# Exam 1 Practice
# Question Number 2
# Biking Mileage

# Initialize variables
new_day = float(input('How many miles did you ride on day 1? '))
total_miles = 0
day = 1

# Runs a loop until the user doesn't input anything
while new_day != '':
    new_day = float(new_day)
    if new_day >= 0:
        total_miles += new_day
        day += 1
    new_day = input('How many miles did you ride on day ' + str(day) + '? (Leave blank to end) ')

# Returns the total number of miles
print('You rode a total of', total_miles, 'miles!')
