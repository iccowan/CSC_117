# Ian Cowan
# Feb 25 2019
# Problem 13 on page 164
# Star Pattern

# Initialize variables
num_stars = 7

# Foreach 0-7 runs a loop
for i in range(7):
    # Loops through 7 times to start and then decreases 1 each time
    stars = num_stars
    while stars > 0:
        # Print a star
        print('*', end='')
        stars = stars - 1

    # Removes one star from the beginning number
    print('\n')
    
    num_stars = num_stars - 1
