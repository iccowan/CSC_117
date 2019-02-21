# Ian Cowan
# Feb 25 2019
# Problem 1 on page 161
# Bug Collector

# Initialize the total_bugs accumulator
total_bugs = 0

# Loop for each day for 5 days
for day in range(1, 6):
    bugs = int(input('How many bugs for today (day ' + str(day) + ')? '))
    total_bugs += bugs

# Returns the total number of bugs at the end of 5 days
print('There were a total of', total_bugs, 'collected.')
