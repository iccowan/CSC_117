# Exam 1 Practice
# Question Number 4
# Mosquito Sickness

# Import Packages
import random

# Get the necessary information from the user
pop = int(input('What would you like the starting population to be? '))
days = int(input('How many days would you like to run the simulation for? '))

# Validation
while pop <= 0:
    pop = int(input('Please enter a valid population: '))

while days <= 0:
    days = int(input('Please enter a valid number of days: '))

# Table Headers
print('Day Number\tNumber of Ill\tNon-Ill Population Remaining')
print('------------------------------------------------------------')

# Initialize Variables
ill = 0
day = 1

# Runs foreach day
while days > 0 and pop > 0:
    # Prints the numbers at the beginning of the day
    print(day, end='\t\t')
    print(ill, end='\t\t')
    print(pop)

    # Runs foreach sick person
    for j in range(ill):
        num = random.randint(1, 100)
        if num >= 17 and num <= 100:
            pop += 1

    # Resets the ill variables
    ill = 0

    # Runs foreach remaining alive person
    for j in range(pop):
        num = random.randint(1, 100)
        if num >= 1 and num <= 43:
            ill += 1
            pop -= 1

    days -= 1
    day += 1

if pop == 0:
    if days != 0:
        print(day, end='\t\t')
        print(ill, end='\t\t')
        print(pop, 'EVERYONE DIED!', sep='\t', end='\n\n')
    print('Everyone died on day', day)
else:
    print('Everyone survived for the duration of the simulation!')
