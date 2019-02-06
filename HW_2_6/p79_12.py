# Ian Cowan
# Feb 06 2019
# Problem 12 on page 79
# Stock Buying/Selling Calculator

# Prompt the user for any applicable information
shares_purchased = float(input('How many shares of stock did you purchase? '))
shares_purchased_cost = float(input('How much did the stock cost per share at purchase? $'))
purchase_commission = float(input('How much was the purchase commission that you paid (in percent)? '))

shares_sold = float(input('How many shares of stock did you sell? '))
shares_sold_cost = float(input('How much did the stock cost per share at time of sale? $'))
sell_commission = float(input('How much was the selling commission that you paid (in percent)? '))

# Make applicable calculations
purchase_total = shares_purchased * shares_purchased_cost
purchase_commission_total = purchase_total * (purchase_commission / 100)

sell_total = shares_sold * shares_sold_cost
sell_commission_total = sell_total * (sell_commission / 100)

total_result = (sell_total + sell_commission_total) - (purchase_total + purchase_commission_total)

# Return the applicable information to the user
print('You initially paid a total of $' + str('{:.2f}'.format(purchase_total)) + ' for the stocks with a commission of $' + str('{:.2f}'.format(purchase_commission_total)))
print('You sold your stocks for a total of $' + str('{:.2f}'.format(sell_total)) + ' with a commission of $' + str('{:.2f}'.format(sell_commission_total)))

if total_result > 0:
    print('You made a total PROFIT of: $' + str('{:.2f}'.format(total_result)))
elif total_result < 0:
    print('You had a total LOSS of: $' + str('{:.2f}'.format(total_result)))
else:
    print('You made no profit and lost no money')
