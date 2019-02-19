# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab08 Loops 1
# 18 Feb 2019

# Begin sleepy loop
# Foreach range 0-9 as i, print the statement
for i in range(10):
    print('You are feeling very sleepy.')
# End sleepy loop

# Begin user message display print
# Prompt the user for applicable inputs
statement = input('What statement would you like to display? ')
iterations = int(input('How many times would you like to print the statement? '))

# Prints the statement the number of times specified by user
for i in range(iterations):
    print(statement)
# End user message display print

# Begin sequences
# Sequence A
print('\nSequence A:')
# Foreach range 1-298 (counting by 3) as num, prints num
for num in range(1, 299, 3):
    print(num)

# Sequence B
print('\nSequence B:')
# Foreach range 0-99 as num, squares num
for num in range(100):
    print(num * num)

# Sequence C
print('\nSequence C:')
num = 1
# Foreach range 0-99 as i, multiplies num by 2
for i in range(100):
    print(num)
    num = num * 2

# Sequence D
print('\nSequence D:')
num = 0
# Foreach range 0-99 as i, adds the index to the previous number for the new number
for i in range(100):
    # Adds one to i to correct for 0-99
    i += 1
    print(num)
    # Adds i to num
    num = num + i

# Sequence E, Rabbit generation
print('\nSequence E:')
num1 = 1
num2 = 1
# Foreach range 0-99 as i, rabbitly generates the number
for i in range(100):
    # If it is the first two, it'll output 1 (preassigned as num1 and num2)
    if i == 0:
        num = num1
    elif i == 1:
        num = num2
    # After the first two, if i is even, it'll append num2
    elif i % 2 == 0:
        num = num1 + num2
        num2 = num
    # If the i is even, it'll append num1
    elif i % 2 != 0:
        num = num1 + num2
        num1 = num
    # Prints the resultant number
    print(num)
# End sequences
