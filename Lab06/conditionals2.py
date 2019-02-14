# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab06 Conditionals 2
# 13 Feb 2019

# Begin Frequent Shopper Points
# Prompt the user to input how much they spent at the shop
dollars = float(input('How much money did you spend? $'))

# Decide how many points the user receives
if dollars >= 0.01 and dollars <= 0.99:
    points = 1
elif dollars >= 1.00 and dollars <= 4.99:
    points = 3
elif dollars >= 5.00 and dollars <= 9.99:
    points = 8
elif dollars >= 10.00:
    points = 20

# Returns the number of points the user receives
print('You get ' + str(points) + ' points for spending $' + str('{:.2f}'.format(dollars)) + '!')
# End Frequent Shopper Points

# Begin Discounts
# Prompts the user to enter price, discount, and quantity and converts values
# if they exist
price = input('How much did the item(s) cost? $')
quantity = input('What quantity of item(s) did you purchase? ')
if quantity != '':
    quantity = int(quantity)
    if quantity >= 1 and quantity <= 5:
        discount = 0.0
    elif quantity >= 6 and quantity <= 14:
        discount = 0.05
    elif quantity >= 15 and quantity <= 26:
        discount = 0.10
    elif quantity >= 27 and quantity <= 35:
        discount = 0.15
    elif quantity >= 36 and quantity <= 43:
        discount = 0.20
    elif quantity >= 44:
        discount = 0.25
else:
    quantity = 'null'
    discount = 0.0

# Checks to make sure the user entered a price
if price != '':
    price = float(price)

    # Runs the required calculations
    if discount != 'null':
        total_per_item = price * (1 - discount)
    else:
        total_per_item = price

    if quantity != 'null':
        total = total_per_item * quantity
        subtotal = price * quantity
    else:
        total = total_per_item
        subtotal = price

    total_saved = subtotal - total

    # Returns the subtotal, discounted total, and money saved
    print('Subtotal:', '$' + str('{:.2f}'.format(subtotal)))
    print('Total after discount:', '$' + str('{:.2f}'.format(total)))
    print('Money saved:', '$' + str('{:.2f}'.format(total_saved)))
else:
    print('Error: You must at least enter a price.')
# End Discounts

# Begin Discounts Tests
# Input: item name  price   quantity    subtotal    discount    total
# Input: backpack   21.75   3           65.25       0.0         65.25
# Input: laptop     1050.65 25          26266.25    2626.63     26266.25
# Input: notebook   4.00    55          220.0       165.0       55.0
# End Discounts Tests

# Begin Leap Years
# Prompts the user for a input year
year = input('What year would you like to check for a leap year? ')

# Checks to see if the year is actually a leap year
if year != '' and (len(year) >= 0 and len(year) <= 4):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, 'is a leap year!')
            else:
                print(year, 'is not a leap year because it is divisible by 100 but not 400')
        else:
            print(year, 'is a leap year!')
    else:
        print(year, 'is not a leap year because it is not divisible by 4')
else:
    print('Error: you must input a year')
# End Leap Years
