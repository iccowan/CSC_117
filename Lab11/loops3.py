# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab11 Loops3
# 25 Feb 2019

# Begin Biggest Value
# Initialize variables
num = input('Enter number 1 (Leave blank to end): ')
i = 1

# While the number entered is not blank, run the loop
while num != '':
    num = float(num)
    if i == 1:
        largest_num = num
    elif num > largest_num:
        largest_num = num
        
    i += 1
    num = input('Enter number ' + str(i) + ' (Leave blank to end): ')

# Return the biggest number entered
print('The biggest number you entered was', largest_num)
# End Biggest Value

# Begin Lowest Temp
# Initialize variables
temp = float(input('What was the temperature at 1 AM? '))
time = 1

# While the time is less than or equal to 9 AM, run the loop
while time <= 9:
    if time != 1:
        temp = float(input('What was the temperature at ' + str(time) + ' AM? '))
    else:
        lowest_temp = temp
        lowest_temp_time = time
        
    if temp < lowest_temp:
        lowest_temp = temp
        lowest_temp_time = time
        
    time += 1

# Return the time and temperature of the lowest temperature
print('The lowest temperature occured at', lowest_temp_time, 'AM and was', lowest_temp, 'degrees')
# End Lowest Temp

# Begin Positive Product
# Initialize variables
num = input('Enter an integer to multiply (Leave blank to end): ')
product = 1

# While the input is not blank, run the loop
while num != '':
    num = int(num)
    if num > 0:
        product *= num
    num = input('Enter an integer to multiply (Leave blank to end): ')

# Return the final product
print('The total product of the positive integers you entered is', product)
# End Positive Product

# Begin Prime Number Checker
# Initialize variables
num = int(input('Enter a Natural Number: '))
prime = True

# Runs a backward range loop to check for prime
for n in range(num - 1, 1, -1):
    if num % n == 0:
        prime = False

# Checks the prime flag and returns appropiate result
if prime:
    print(num, 'is PRIME!')
else:
    print(num, 'is NOT PRIME!')
# End Prime Number Checker
