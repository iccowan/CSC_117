# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Final Project Forest Fire
# 08 May 2019
# Main File

# Import Packages
from Forest import Forest
from Tree import Tree
from graphics import *

# Define createButton()
# Inputs:
#   int typeOfButton
#   Window win
# Outputs:
#   Rectangle btn
def createButton(typeOfButton, win):
    # Create a point and text depending on which button
    if typeOfButton == 0:
        text = Text(Point(150, 50), "Regrow Forest")
        btn = Rectangle(Point(130, 45), Point(170, 55))
        btn.setFill("lightgray")
    else:
        text = Text(Point(150, 30), "Exit")
        btn = Rectangle(Point(130, 25), Point(170, 35))
        btn.setFill("lightgray")

    # Draw them
    btn.draw(win)
    text.draw(win)

    return btn

# Define getTreeAndPercent
# Inputs:
#   Window win
#   Forest forest
#   Entry entry
# Outputs:
#   Tree tree
#   float percent
def getTreeAndPercent(win, forest, entry):
    # do-while loop simulation
    isFloat = False
    burnPercent = 1.2
    i = 0
    while (not isFloat) or (0 > burnPercent or 1 < burnPercent):
        # If this isn't the first run, tell them their error
        if i > 0:
            throwError("Invalid probability.")

        clickpt = win.getMouse()

        # Check and see if the click is inside of a tree
        inTree = forest.clickInTree(clickpt)

        # Wait for a click on a tree
        while inTree is None:
            clickpt = win.getMouse()

            # Check and see if the click is inside of a tree
            inTree = forest.clickInTree(clickpt)

        # Get the input in the box
        burnPercent = entry.getText()

        # Try to make the input into a float
        # If it doesn't work, wait until it's a valid number
        try:
            burnPercent = float(burnPercent)
            isFloat = True
        except ValueError:
            isFloat = False

        i += 1

    return inTree, burnPercent

# Define throwError()
# Inputs:
#   String err
# Outputs:
#   NONE
def throwError(err):
    # Create another window
    win = GraphWin("Error", 300, 100)

    # Create text with the message
    txt = Text(Point(150, 50), "ERROR: " + err)
    txt.draw(win)

# Define main()
def main():
    # Init the forest
    forest = Forest()
    win = forest.getWindow()

    # Draw an input box
    e = Entry(Point(150, 75), 10)
    e.setFill("white")
    e.draw(win)

    # Draw the text above the box
    text1 = Text(Point(150, 86), "Probability of Spreading")
    text = Text(Point(150, 81), "Enter 0-1 (Ex. 0.25)")
    text1.draw(win)
    text.draw(win)

    # Draw two buttons
    createButton(0, win)
    createButton(1, win)

    # Finally, run the simulation!
    closeProgram = False

    while not closeProgram:
        # Get the selected tree and burn probability
        tree, burnPercent = getTreeAndPercent(win, forest, e)

        # Begin the fire!
        forest.beginBurn(tree, burnPercent)

        forest.displayPercentBurned()

        # Get a click and see if they want to close the program
        # or if they want to reset and go again
        clickpt = win.getMouse()

        while not(clickpt.getX() <= 170 and clickpt.getX() >= 130 and \
                  ((clickpt.getY() <= 55 and clickpt.getY() >= 45) or \
                  (clickpt.getY() <= 35 and clickpt.getY() >= 25))):
            # Get another click
            clickpt = win.getMouse()

        if clickpt.getX() <= 170 and clickpt.getX() >= 130 and \
           clickpt.getY() <= 55 and clickpt.getY() >= 45:
            # Reset the forest
            forest.resetForest()
        elif clickpt.getX() <= 170 and clickpt.getX() >= 130 and \
             clickpt.getY() <= 35 and clickpt.getY() >= 25:
            # Close the window
            closeProgram = True

# Call main()
main()
