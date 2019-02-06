# Challenge 2/6/19
# Testing Python Formatting

# Dividing and then go to 4 decimal places
print('10 divided by 3 =', '{:.4f}'.format(10 / 3))

# Dividing and then go to scientific notation
print('7000 divided by 3 =', '{:.2e}'.format(7000 / 3))

# Printing a very large number with commas
print('{:,}'.format(12345678.23445667))

# Printing a very large number with commas and only one decimal place
print('{:,.1f}'.format(12345678.23445667))

# Printing a small decimal as a percent
print('{:.2%}'.format(0.643))
