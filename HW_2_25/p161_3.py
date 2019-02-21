# Ian Cowan
# Feb 25 2019
# Problem 3 on page 161
# Budget Analysis

# Prompts the user for their monthly budget
bud = float(input('What is your budget for this month? $'))

# Initialize variables for Loop
print('Enter the cost of each of your expenses for the month. Press "enter" when you\'re finished.')
spend = input('$')
total = 0.0

# Loop to continue prompting the user to enter their spendings until they want to stop
while spend != '':
    spend = float(spend)
    total += spend
    spend = input('$')

# Calculates the amount the user is over or under budget
bud_total_diff = bud - total

# Checks the difference between budget and total and returns
if bud_total_diff > 0:
    print('Congratulations! You are $' + str('{:3,.2f}'.format(bud_total_diff)) + ' under budget this month!')
elif bud_total_diff == 0:
    print('Cutting it close! You were exactly on budget this month.')
else:
    print('Whoops, you were $' + str('{:3,.2f}'.format(bud_total_diff * -1)) + ' over budget this month.')
