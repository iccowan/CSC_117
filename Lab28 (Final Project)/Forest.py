# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Final Project Forest Fire
# 08 May 2019
# FOREST CLASS

# Import Packages
from graphics import *
from Tree import Tree
import time

# Class Forest
# Attributes:
#   Window __win
#   dict<tuple : Tree> __trees
#   tuple __tupledPoint
#   Text __percentBurn
# Methods:
#   Window getWindow()
#   dict<tuple : Tree> getTrees()
#   void clearForest()
#   Tree clickInTree(Point)
#   void beginBurn(Tree, float)
class Forest:
    # Construct Forest
    def __init__(self):
        # Create a window and set that as an attribute
        window = GraphWin("Forest Fire Simulator, by Ian Cowan", 800, 400)
        window.setCoords(0, 0, 200, 100)
        self.__win = window

        # Init the stuff inside the window
        rect = Rectangle(Point(0, 0), Point(100, 100))
        rect.setFill("white")
        rect.draw(window)

        # Draw borders
        for i in range(0, 101, 10):
            b = Rectangle(Point(i - 0.01, 0), Point(i + 0.01, 100))
            b.draw(window)

        for i in range(0, 101, 10):
            b = Rectangle(Point(0, i - 0.01), Point(100, i + 0.01))
            b.draw(window)

        # Create the trees and add them to a dictionary
        trees = dict()
        for i in range(5, 96, 10):
            for j in range(5, 96, 10):
                # Add the tupled point (1,1) ... (10, 10)
                if len(str(i)) == 1:
                    pointI = 1
                else:
                    pointI = int(str(i)[0]) + 1

                if len(str(j)) == 1:
                    pointJ = 1
                else:
                    pointJ = int(str(j)[0]) + 1

                # Create the tree and add it to the dictionary
                t = Tree(Point(i, j), window, (pointI, pointJ))
                trees[(pointI, pointJ)] = t
                self.__tupledPoint = (pointI, pointJ)

        # Add the trees as an attribute
        self.__trees = trees
        self.__percentBurn = Text(Point(0, 0), "Initalizing...")

    # Returns the window
    def getWindow(self):
        return self.__win

    # Returns the dictionary of all the trees
    def getTrees(self):
        return self.__trees

    # Resets the forest
    def resetForest(self):
        for t in self.__trees:
            self.__trees[t].reset()

    # Checks to see if a click is inside of a tree
    # Returns the tree if so, returns None if not
    def clickInTree(self, clickpt):
        inTree = None
        for t in self.__trees:
            tree = self.__trees[t]
            anchor = tree.anchorPoint()

            if (clickpt.getX() < anchor.getX() + 5) and (clickpt.getX() > anchor.getX() - 5) and \
               (clickpt.getY() < anchor.getY() + 5) and (clickpt.getY() > anchor.getY() - 5) and \
               (inTree is None):
                inTree = self.__trees[t]

        return inTree

    # Begins the burning in the forest
    def beginBurn(self, tree, burnPercent):
        allTrees = self.__trees

        # First burn the tree
        tree.startBurn(allTrees, burnPercent, 1)

        # Wait
        stillBurning = True
        round = 1

        # Check each tree for burning
        while stillBurning:
            needMoreUpdates = list()
            for t in allTrees:
                #if allTrees[t].getNextState() > 0 and allTrees[t].getEarliestBurnRound() == -1:
                #    allTrees[t].setBurnRound(round)

                needAnotherUpdate = allTrees[t].update(allTrees, burnPercent, round)
                needMoreUpdates.append(needAnotherUpdate)

            # Wait
            time.sleep(0.7)

            if True not in needMoreUpdates:
                stillBurning = False

            round += 1

    # Displays the amount of the forest burned
    def displayPercentBurned(self):
        allTrees = self.__trees

        # Loops through each tree and checks to see how many are
        # at their burned state (3)
        bT = 0
        totalTrees = 0  # Should be 100, but safer to check
        for t in allTrees:
            if allTrees[t].getState() == 3:
                bT += 1

            totalTrees += 1

        percent = int((bT / totalTrees) * 100)

        # Put the percent on the screen
        self.__percentBurn.undraw()
        self.__percentBurn = Text(Point(150, 65), str(percent) + "% of the forest burned down!")
        self.__percentBurn.draw(self.__win)
