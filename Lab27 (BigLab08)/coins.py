# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab08 Coins
# 19 Apr 2019
# Main File

# Import Dependencies
from graphics import *
from Coin import Coin

# Define initWindow()
# Inputs:
#   NONE
# Outputs:
#   Window win
def initWindow():
    # Create the window and set the coordinates
    win = GraphWin("100 Coins", 700, 700)
    win.setCoords(0, 0, 100, 100)
    win.setBackground("gray")

    # Draw the grid on the window
    # Horizontal lines
    for i in range(1, 10):
        # Create a rectangle with the appropiate coordinates
        p1 = Point(i * 10 - 0.01, 0)
        p2 = Point(i * 10 + 0.01, 100)

        rect = Rectangle(p1, p2)
        rect.draw(win)

    # Vertical lines
    for i in range(1, 10):
        # Create a rectangle with the appropiate coordinates
        p1 = Point(0, i * 10 - 0.01)
        p2 = Point(100, i * 10 + 0.01)

        rect = Rectangle(p1, p2)
        rect.draw(win)

    return win

# Define createCoins()
# Inputs:
#   Window win
# Outputs:
#   list<Coin> coins
def createCoins(win):
    # Create 100 points and add them to a list
    # Init list
    coins = list()
    
    # Each row
    for i in range(5, 100, 10):
        # Each column
        for j in range(5, 100, 10):
            pt = Point(i, j)
            if i == 95 and j == 95:
                c = Coin(win, pt, True)
            else:
                c = Coin(win, pt, False)
            coins.append(c)

    return coins

# Define flipCoins()
# Inputs:
#   list<Coin> coins
#   Point click
# Outputs:
#   boolean isWinClosed
def flipCoins(coins, click):
    # Assume the window is not closing
    isWinClosed = False
    
    # Loops through each coin
    for c in coins:
        coinBoolList = c.clicked(click)
        if coinBoolList[0]:
            c.flip()

        if coinBoolList[1]:
            isWinClosed = True
    
    return isWinClosed

# Define main()
def main():
    # Init the window
    window = initWindow()

    # Create 100 coins
    coins = createCoins(window)

    isWinClosed = False

    # Run until the closing coin is clicked
    while not isWinClosed:
        # Wait for the user to click
        click = window.getMouse()
        
        # Check and see if the click was inside of a circle
        isWinClosed = flipCoins(coins, click)

# Call main()
main()
