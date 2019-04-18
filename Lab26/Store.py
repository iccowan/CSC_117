# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab26 OOPS 2
# 17 Apr 2019
# MAIN

# Import Classes
from Customer import Customer
from Item import Item

# Define initCustomersItems()
# Inputs:
#   NONE
# Outputs:
#   dict[String customerName : Customer] customers
#   dict[String itemName : Item] items
def initCustomersItems():
    # Open files
    items_file = open('inventory.csv', 'r')
    customers_file = open('customers.csv', 'r')

    # Skip first lines, title lines of csv
    items_file.readline()
    customers_file.readline()

    # Init variabls
    customers = dict()
    items = dict()

    # Loop through each file and add their values to a list
    for line in items_file:
        # Split the csv record
        line = line.strip()
        splitLine = line.split(',')

        # Create item instance
        item = Item(splitLine[0], float(splitLine[1]), splitLine[2], int(splitLine[3]))

        # Add the item to the dictionary
        items[item.getName()] = item

    for line in customers_file:
        # Split the csv record
        line = line.strip()
        splitLine = line.split(',')

        # Create customer instance
        cust = Customer(splitLine[0], splitLine[1], splitLine[2], float(splitLine[3]))

        # Add the item to the dictionary
        customers[cust.getFullName()] = cust

    # Close files
    items_file.close()
    customers_file.close()

    return customers, items

# Define getUserInput()
# Inputs:
#   NONE
# Outputs:
#   int choice
def getUserInput():
    # List the options
    print("Choose an option from the list below:")
    print("1 - List Inventory")
    print("2 - Add Item")
    print("3 - Search Inventory")
    print("4 - Delete Item")
    print("5 - Create Customer")
    print("6 - Delete Customer")
    print("7 - Update Customer")
    print("8 - Exit")

    # Get their choice
    choice = int(input())

    # Make sure the choice is 1-8
    while choice < 1 or choice > 8:
        print("The only valid choices are 1-8")
        choice = int(input())

    return choice

# Define listInventory()
# Inputs:
#   dict[String itemName : Item] items
# Outputs:
#   NONE
def listInventory(items):
    # Print out all of the inventory
    print("Current Inventory:")

    for k in items:
        print(items[k])

# Define addItem()
# Inputs:
#   dict<Item> items
# Outputs:
#   NONE
def addItem(items):
    print("Create a New Item...")
    # Get the inputs for the initial attempt
    name = input("Item Name: ")
    price = float(input("Item Price: $"))
    itemType = input("Item Type: ")
    quantity = int(input("Quantity: "))

    # Confirms that the information is correct
    confirm = input("Do you want to create " + str(quantity) + " " + name + \
              "(s) of the type " + itemType + " costing $" + str("{:.2f}".format(price)) + "? [y/n]")

    while confirm.upper() == 'N':
        # Try again
        # Get the inputs for the next attempt(s)
        name = input("Item Name: ")
        price = float(input("Item Price: "))
        itemType = input("Item Type: ")
        quantity = int(input("Quantity: "))

        # Confirms that the information is correct
        confirm = input("Do you want to create " + str(quantity) + " " + name + \
                  "(s) of the type " + itemType + " costing $" + str("{:.2f}".format(price)) + "? [y/n]")

    # Create the instance of Item
    item = Item(name, price, itemType, quantity)

    # Add the instance to the dictionary
    items[name] = item

    print("The item has been added!")

# Define searchInventory()
# Inputs:
#   dict[String itemName : Item] items
# Outputs:
#   NONE
def searchInventory(items):
    # Get the user's search
    search = input("What item would you like to search for? ").upper()

    # Search for the item in the dictionary
    result = None
    for k in items:
        if items[k].getName().upper() == search and result is None:
            result = items[k]

    if result is not None:
        # Print something
        print("Results Found for " + search + ":")
        print(result)
    else:
        # Print the item
        print("No results found for " + search)

# Define deleteItem()
# Inputs:
#   dict[String itemName : Item] items
# Outputs:
#   NONE
def deleteItem(items):
    # Turn every item into a list for listing
    itemsList = list()
    for k in items:
        itemsList.append(k)

    # Print the items to choose from
    i = 0
    print("Choose an item to delete:")
    for it in itemsList:
        print(i, "-", items[it])

        i += 1

    # Get the user input
    userInput = int(input())

    # Validation
    while userInput < 0 or userInput > len(itemsList) - 1:
        print("Invalid item, enter a valid number:")
        userInput = int(input())

    # Tell the user what they're doing
    itemName = str(items[itemsList[userInput]])
    print("Deleting " + itemName + "...")

    # Remove item from dictionary, no need to remove from list
    del items[itemsList[userInput]]

    # Remind the user what they did
    print("Deleted " + itemName + "!")

# Define createCustomer()
# Inputs:
#   dict[String customerName : Customer] customers
# Outputs:
#   NONE
def createCustomer(customers):
    print("Create a New Customer...")
    # Get the inputs for the initial attempt
    fname = input("First Name: ")
    lname = input("Last Name: ")
    email = input("Email: ")
    moneySpent = float(input("Current Money Spent: $"))

    # Confirms that the information is correct
    confirm = input("Do you want to add " + fname + " " + lname + " " + " with email " + \
              email + " that has spent $" + str("{:.2f}".format(moneySpent)) + "? [y/n]")

    while confirm.upper() == 'N':
        # Try again
        # Get the inputs for the next attempt(s)
        fname = input("First Name: ")
        lname = input("Last Name: ")
        email = input("Email: ")
        moneySpent = float(input("Current Money Spent: $"))

        # Confirms that the information is correct
        confirm = input("Do you want to add " + fname + " " + lname + " " + " with email " + \
                  email + " that has spent $" + str("{:.2f}".format(moneySpent)) + "? [y/n]")

    # Create the instance of Item
    cust = Customer(lname, fname, email, moneySpent)

    # Add the instance to the dictionary
    customers[cust.getFullName()] = cust

    print("The customer has been added!")

# Define deleteCustomer()
# Inputs:
#   dict[String customerName : Customer] customers
# Outputs:
#   NONE
def deleteCustomer(customers):
    # Turn every cust into a list for listing
    custList = list()
    for k in customers:
        custList.append(k)

    # Print the custs to choose from
    i = 0
    print("Choose a customer to delete:")
    for it in custList:
        print(i, "-", customers[it])

        i += 1

    # Get the user input
    userInput = int(input())

    # Validation
    while userInput < 0 or userInput > len(custList) - 1:
        print("Invalid customer, enter a valid number:")
        userInput = int(input())

    # Tell the user what they're doing
    custName = str(customers[custList[userInput]])
    print("Deleting " + custName + "...")

    # Remove item from dictionary, no need to remove from list
    del customers[custList[userInput]]

    # Remind the user what they did
    print("Deleted " + custName + "!")

# Define updateCustomer()
# Inputs:
#   dict[String customerName : Customer] customers
# Outputs:
#   NONE
def updateCustomer(customers):
    # Turn every cust into a list for listing
    custList = list()
    for k in customers:
        custList.append(k)

    # Print the custs to choose from
    i = 0
    print("Choose a customer to update:")
    for it in custList:
        print(i, "-", customers[it], "-", customers[it].getMoneySpentStr())

        i += 1

    # Get the user input
    userInput = int(input())

    # Validation
    while userInput < 0 or userInput > len(custList) - 1:
        print("Invalid customer, enter a valid number:")
        userInput = int(input())

    # Get the amount they want to change their spending amount to
    amount = float(input("How much have they spent? $"))

    # Tell the user what they're doing
    custName = str(customers[custList[userInput]])
    print("Updating " + custName + "...")

    # Remove item from dictionary, no need to remove from list
    customers[custList[userInput]].setMoneySpent(amount)

    # Remind the user what they did
    print("Updated " + custName + "!")

# Define saveCustomersItems()
# Inputs:
#   dict[String customerName : Customer] customers
#   dict[String itemName : Item] items
# Outputs:
#   NONE
def saveCustomersItems(customers, items):
    # Reopen the files to write
    cust_file = open("customers.csv", 'w')
    items_file = open("inventory.csv", 'w')

    # Loop through each dictionary and add them to the files
    cust_file.write("lname,fname,email,moneySpent\n")
    for k in customers:
        c = customers[k]
        stringToAdd = c.getLastName() + ',' + c.getFirstName() + ',' + \
                      c.getEmail() + ',' + str(c.getMoneySpent()) + "\n"

        cust_file.write(stringToAdd)

    items_file.write("name,cost,type,quantity\n")
    for k in items:
        i = items[k]
        stringToAdd = i.getName() + ',' + str(i.getPrice()) + ',' + \
                      i.getType() + ',' + str(i.getQuantity()) + "\n"

        items_file.write(stringToAdd)

    # Close files
    cust_file.close()
    items_file.close()

# Define main()
def main():
    # Get all of the customers and items
    customers, items = initCustomersItems()

    # Get the user input
    userInput = getUserInput()

    # Wait until they want to exit
    while userInput != 8:
        # Line Break
        print()

        # 1 - List Inventory
        if userInput == 1:
            # Call listInventory()
            listInventory(items)
        # 2 - Add Item
        elif userInput == 2:
            # Call addItem()
            addItem(items)
        # 3 - Search Inventory
        elif userInput == 3:
            # Call searchInventory()
            searchInventory(items)
        # 4 - Delete Item
        elif userInput == 4:
            # Call deleteItem()
            deleteItem(items)
        # 5 - Create Customer
        elif userInput == 5:
            # Call createCustomer()
            createCustomer(customers)
        # 6 - Delete Customer
        elif userInput == 6:
            # Call deleteCustomer()
            deleteCustomer(customers)
        # 7 - Update Customer
        elif userInput == 7:
            # Call updateCustomer()
            updateCustomer(customers)

        # Line break(s) to clear screen
        print()

        # Reask the user what they want to do the next time around
        userInput = getUserInput()

    # Save changes (Doesn't update the list everytime to save time)
    print("Saving all changes...")
    saveCustomersItems(customers, items)

    # Print exit message
    print("Exiting...")

# Call main()
main()
