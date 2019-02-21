# Ian Cowan
# Feb 25 2019
# Problem 14 on page 164
# Hashtag Pattern

# Initializes variables
spaces_tot = 0

# Foreach 0-6, runs a Loop
for i in range(6):
    # First hashtag
    print('#', end='')
    # While loop for spaces
    spaces = spaces_tot
    while spaces > 0:
        print(' ', end='')
        spaces = spaces - 1
    # Second hashtag
    print('#')

    spaces_tot += 1
