# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab03 Fish Tank Ammonia
# 3 Mar 2019
# Fish Tank Ammonia

# Prompt user for all variables
days = int(input('How many days would you like the simulation to run for? '))
total_days = days
num_fish = int(input('How many fish are you starting with? '))
ammonia_per_day = float(input('How much ammonia is produced per fish per day (in mg)? '))
toxic_level = float(input('How much ammonia is toxic to the fish (in mg)? '))
h20_replace = float(input('What percentage of water is replaced every n days (%)? '))
replace_interval = int(input('How many days pass before changing the water? '))

# Validation loops
while days <= 0:
    print('Your number of days must be positive and greater than zero.')
    days = int(input('How many days would you like the simulation to run for? '))

while num_fish <= 0:
    print('Your numer of fish must be positive and greater than zero.')
    num_fish = int(input('How many fish are you starting with? '))

while ammonia_per_day <= 0:
    print('The ammonia produced per day per fish must be positive and greater than zero.')
    ammonia_per_day = float(input('How much ammonia is produced per fish per day (in mg)? '))

while toxic_level <= 0:
    print('The toxic level of ammonia should be positive and greater than zero.')
    toxic_level = float(input('How much ammonia is toxic to the fish (in mg)? '))

while h20_replace <= 0:
    print('The percentage of water you replace must be positive and greater than zero.')
    h20_replace = float(input('What percentage of water is replaced every n days? '))

while replace_interval <= 0:
    print('The interval which you replace the water must be positive and greater than zero.')
    replace_interval = int(input('How many days pass before changing the water? '))

# Adds table headers
print('')
print('Day Number\tAmmonia Present (mg)')
print('------------------------------------')

# Runs a loop until all the days have passed OR all the fish are dead
day = 1
ammonia_level = 0

while num_fish > 0 and days > 0:
    if ammonia_level >= toxic_level:
        # Kills all fish
        num_fish = 0
        
    if day % replace_interval == 0:
        # Removes ammonia
        ammonia_level = ammonia_level - (ammonia_level * (h20_replace / 100))

    if num_fish != 0:
        # Prints variables
        print(str(day) + '\t\t' + str('{:.2f}'.format(ammonia_level)))
        
        # Updates all variables for the end of the day if the fish aren't dead
        day += 1
        ammonia_level += ammonia_per_day * num_fish
        days = days - 1
    else:
        # Prints variables - DEAD
        print(str(day) + '\t\t' + str('{:.2f}'.format(ammonia_level)) + '\t\tDEAD!')

# Checks for the number of fish remaining and returns accordingly
print('')
if num_fish == 0 and days != 0:
    print('All of the fish died after day', day)
else:
    print('The fish lived for all', total_days, 'days!')
