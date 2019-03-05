# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab13 Functions 1
# 04 Mar 2019

# Define integerFactorial()
# Inputs:
#   int: integer
# Outputs:
#   int: total
def integerFactorial(integer):
    # Initialize variables for loop
    total = 1

    # Runs a loop and multiplies until all the numbers have be included
    while integer > 0:
        total *= integer
        integer -= 1

    # Returns the total
    return total

# Define primeNumber()
# Inputs:
#   int: number
# Outputs:
#   boolean: result
def primeNumber(number):
    # Checks for the case that number is less than 2
    if number < 2:
        result = False
    else:
        # Initialize variables
        result = True
        i = number - 1

        # Loops through each number before i = 1 but stops if it is not prime
        while i > 1 and result == True:
            if number % i == 0:
                result = False
            i -= 1

    # Return True for prime, False for not prime
    return result

# Define main()
def main():
    # Begin hello and goodbye world
    print('Hello, world')
    print('Goodbye, world')
    # End hello and goodbye world

    # Begin factorials
    # Prompt the user for the integer for the function
    n = int(input('What would you like to compute the factorial for? '))

    # Call integerFactorial()
    f = integerFactorial(n)

    # Return the result
    print('The factorial of', n, 'is', f)
    # End factorials

    # Begin prime numbers
    number = int(input('What number would you like to check for prime? '))

    # Call primeNumber()
    prime = primeNumber(number)

    # Return depending on prime
    if prime:
        print('The number,', number, 'is prime!')
    else:
        print('The number,', number, 'is not prime.')
    # End prime numbers

    # Begin first 1000 prime numbers
    # Initialize variables for loop
    i = 1
    current_number = 1

    # Loops until there are 1000 primes
    while i <= 1000:
        # Call primeNumber()
        prime = primeNumber(current_number)

        # Checks to see if it is prime
        if prime:
            # Returns the number
            # Ordering
            if i % 10 == 0:
                print(current_number)
            else:
                print(current_number, end='\t')

            # Adds one to index
            i += 1

        # Adds one to current_number
        current_number += 1
    # End first 1000 prime numbers

# Call main()
main()
