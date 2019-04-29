# Create a file with first 20 primes skipping 100 each time

def checkForPrime(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0 and num != 2:
            isPrime = False

    return isPrime
        

def main():
    # open file
    f = open('primes.txt', 'w')
    num_primes = 0
    i = 2

    while i < 1000:
        isPrime = checkForPrime(i)
        if isPrime:
            f.write(str(i) + "\n")
            print(i)
            num_primes += 1

        i += 1

    f.close()
    
main()
