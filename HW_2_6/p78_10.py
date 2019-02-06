# Ian Cowan
# Feb 06 2019
# Problem 10 on page 78
# Ingredient Calculator for Cookies

# Prompt the user for the number of cookies they would like to make
cookies = int(input('How many cookies do you plan on making? '))

# Sets the variables for the number of cups for ingredients and the number of cookies for those amounts
sugar = 1.5
butter = 1.0
flour = 2.75
total_cookies = 48.0

# Calculates the proportion of cookies the user wants to make vs the number the amounts make
rat = cookies / total_cookies

# Calculates the number of cups for each ingredient for the user to use when cooking
u_sugar = sugar * rat
u_butter = butter * rat
u_flour = flour * rat

# Tells the user how many cups of each ingredient should be used
print('You should use the amounts of the following ingredients to make' + str(int(cookies)) + 'cookies:')
print('Sugar:', '{:.2f}'.format(u_sugar), 'cups')
print('Butter:', '{:.2f}'.format(u_butter), 'cups')
print('Flour:', '{:.2f}'.format(u_flour), 'cups')
