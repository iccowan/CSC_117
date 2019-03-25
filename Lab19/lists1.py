# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab19 Lists 1
# 25 Mar 2019

# Define moviesList()
# Inputs:
#   NONE
# Outputs:
#   list: movies
def moviesList():
    # Open movies.txt
    file_in = open('movies.txt', 'r')

    # Init the list
    movies = list()

    # Loop through the file and add movies to the list
    for mov in file_in:
        movies.append(mov.rstrip('\n'))

    # Close movies.txt
    file_in.close()

    # Append Top Gun to the end of movies
    movies.append('Top Gun')

    # Print all of the movies
    for m in movies:
        print(m)

    return movies

# Define complicateLen()
# Inputs:
#   list: l
# Outputs:
#   int: length
def complicateLen(l):
    # Init variables
    length = 0

    # Loop through each item and add one
    for i in l:
        length += 1

    return length

# Define complicateIn()
# Inputs:
#   list: l
#   str: look_for
# Outputs:
#   bool: exists
def complicateIn(l, look_for):
    # Init variables
    exists = False

    # Loop through the list and see if look_for is in it
    for item in l:
        if item == look_for:
            exists = True

    return exists

# Define complicateSplice()
# Inputs:
#   list: l
# Outputs:
#   list: new_l
def complicateSplice(l):
    # Get length of l and how many items is half
    half_of_l = len(l) // 2

    # Init variables
    first_half = list()
    last_half = list()
    new_l = list()

    # Loop through each index and create 2 new lists
    # first_half, last_half
    for i in l:
        if half_of_l > 0:
            first_half.append(i)
            half_of_l -= 1
        else:
            last_half.append(i)

    # Loop through each list and create a new list
    for j in last_half:
        new_l.append(j)

    for k in first_half:
        new_l.append(k)

    return new_l

# Define complicateIndex()
# Inputs:
#   list: l
#   int: position
# Outputs:
#   str: mov
def complicateIndex(l, position):
    # Init variables
    i = 1

    for j in l:
        if i == position:
            mov = j

        i += 1

    return mov

# Define complicateReverse()
# Inputs:
#   list: li
# Outputs:
#   list: rev_l
def complicateReverse(li):
    # Reverse the list without reverse()
    rev_l = li[::-1]

    return rev_l

# Define complicateMin()
# Inputs:
#   list: l
# Outputs:
#   str: min_val
def complicateMin(l):
    # Init variables
    min_val = l[0]
    
    # Loop through each value and see if it is smaller than the smallest
    for i in l:
        if i < min_val:
            min_val = i

    return min_val

# Define complicateMax()
# Inputs:
#   list: l
# Outputs:
#   str: max_val
def complicateMax(l):
    # Init variables
    max_val = l[0]
    
    # Loop through each value and see if it is bigger than the biggest
    for i in l:
        if i > max_val:
            max_val = i

    return max_val

# Define main()
def main():
    # Call moviesList()
    movies = moviesList()

    # Print the number of movies
    print('Total number of movies:', len(movies))

    # Call complicateLen()
    print('Total number of movies:', complicateLen(movies))

    # Determine if Adventures in Babysitting is in movies
    if 'Adventures in Babysitting' in movies:
        print('YES')
    else:
        print('NO')

    # Call complicateIn()
    if complicateIn(movies, 'Adventures in Babysitting'):
        print('YES')
    else:
        print('NO')

    # Move last half of list to beginning
    num_movies_half = len(movies) // 2
    last_half_movies = movies[num_movies_half:]
    first_half_movies = movies[:num_movies_half]
    movies = last_half_movies + first_half_movies
    print(movies)

    # Call complicateSplice()
    movies = complicateSplice(movies)
    print(movies)

    # Print the 5th item in movies
    print(movies[4])

    # Call complicateIndex()
    print(complicateIndex(movies, 5))

    # Reverse movies
    movies.reverse()
    print(movies)

    # Fix the order to complicate
    movies.reverse()
    
    # Call complicateReverse
    print(complicateReverse(movies))

    # Sort the movies
    movies.sort()
    print(movies)

    # No sorting complication!

    # Find min and max
    print('Minimum movie:', min(movies))
    print('Maximum movie:', max(movies))

    # Call complicateMin()
    print('Minimum movie:', complicateMin(movies))
    # Call complicateMax()
    print('Maximum movie:', complicateMax(movies))

    # Insert Spaceballs into position 5 in movies
    movies.insert(4, 'Spaceballs')
    print(movies)

    # Remove Ferris Bueller's Day Off from movies
    movies.remove('Ferris Bueller\'s Day Off')
    print(movies)

    # Print the index of The Goonies
    print(movies.index('The Goonies'))

# Call main()
main()
