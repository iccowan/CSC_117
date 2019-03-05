# Ian Cowan
# Mar 04 2019
# Problem 13 on page 231
# Falling Distance

# Define fallingDistance()
# Inputs:
#   int: time
# Outputs:
#   float: distance
def fallingDistance(time):
    # Set the gravity constant
    g = 9.8

    # Calculate falling distance
    distance = (0.5 * g) * (time ** 2)

    # Returns the distance
    return distance

# Define main()
def main():
    # Loops though 1-10 and returns the distance for that time
    for i in range(1, 11):
        # Call fallingDistance()
        distance = fallingDistance(i)

        # Return the distance
        print('Distance for time ', i, ': ', '{:.2f}'.format(distance), sep='')

# Call main()
main()
