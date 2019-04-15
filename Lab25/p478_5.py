# Ian Cowan
# Apr 15 2019
# Lab Partner: Jake Pfaller
# Problem 5 on page 478
# RetailItem Class

# Create the RetailItem Class
# Attributes:
#   String __desc
#   int __units
#   float __price
# Methods:
#   NONE
class RetailItem:
    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price

    def __str__(self):
        return self.__desc + " (" + str(self.__units) + " x $" + str(self.__price) + ")"

# Define main()
def main():
    # Create 3 retail items
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Print the items
    print(item1)
    print(item2)
    print(item3)

# Call main()
main()
