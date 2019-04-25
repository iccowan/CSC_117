# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Final Project Forest Fire
# 08 May 2019
# TREE CLASS

# Import Packages
from graphics import *
import random
import time

# Class Tree
# Attributes:
#   Point __pt
#   Image __treeImg
#   Window __win
#   int __state
#   tuple __coords
#   boolean __burnThisRound
#   int __earliestBurnRound
# Methods:
#   void reset()
#   Point anchorPoint()
class Tree:
    # Construct Tree
    def __init__(self, pt, win, coords):
        self.__pt = pt
        self.__win = win
        self.__state = 0
        self.__nextState = 0
        self.__coords = coords
        self.__burnThisRound = False
        self.__earliestBurnRound = -1

        # Draw the tree and store it
        img = Image(pt, "tree.png")
        img.draw(win)
        self.__treeImg = img

    # Resets the state of the tree
    def reset(self):
        self.__state = 0
        self.__nextState = 0
        self.__burnThisRound = False
        self.__earliestBurnRound = -1
        self.__treeImg.undraw()

        newTree = Image(self.__treeImg.getAnchor(), "tree.png")
        newTree.draw(self.__win)
        self.__treeImg = newTree

    # Returns the anchor point
    def anchorPoint(self):
        return self.__treeImg.getAnchor()

    # Returns the tuple coordinates of the tree
    def getCoords(self):
        return self.__coords

    # Returns the next state
    def getNextState(self):
        return self.__nextState

    # Returns the current state
    def getState(self):
        return self.__state

    # Returns the earliest burn round
    def getEarliestBurnRound(self):
        return self.__earliestBurnRound

    # Sets the tree to burn on the next go around
    def setBurn(self):
        self.__nextState = 1

    # Sets the tree to burn this round
    def setBurnRound(self, round):
        self.__burnThisRound = True
        self.__earliestBurnRound = round

    # Sets the next state
    def setNextState(self, state):
        self.__nextState = state

    # Burns the specified tree and checks to see if the trees around should burn
    def startBurn(self, allTrees, burnPercent, round):
        self.__state = 1
        self.__nextState = 2
        self.setBurnRound(2)
        img = self.__treeImg
        img.undraw()

        # Draw the small burn tree
        newImg = Image(self.__treeImg.getAnchor(), "little_burn.png")
        newImg.draw(self.__win)
        self.__treeImg = newImg

        self.checkForAdjacentBurn(allTrees, burnPercent, round)

    def checkForAdjacentBurn(self, allTrees, burnPercent, round):
        # Take the tree and find the 4 adjacent trees
        coords = self.__coords
        adjTree1 = (coords[0], coords[1] - 1)
        adjTree2 = (coords[0], coords[1] + 1)
        adjTree3 = (coords[0] - 1, coords[1])
        adjTree4 = (coords[0] + 1, coords[1])
        adjTrees = [adjTree1, adjTree2, adjTree3, adjTree4]

        # Loop through each tree and see if it is in the forest
        # Also check to see if it's on fire
        # If it's not, check to see if it should be on fire next round
        for t in adjTrees:
            if t in allTrees:
                if allTrees[t].__nextState == 0:
                    randPercent = random.random()
                    if randPercent <= burnPercent:
                        allTrees[t].setBurnRound(round + 1)
                        allTrees[t].setNextState(1)

    # Updates the tree
    def update(self, allTrees, burnPercent, round):
        needAnotherUpdate = True

        if self.__nextState > 0 and self.__state < 3 and self.__burnThisRound and \
           self.__earliestBurnRound <= round and self.__earliestBurnRound != -1:
            # Draw the appropiate photo for the next state
            if self.__nextState == 1:
                self.startBurn(allTrees, burnPercent, round)
                needAnotherUpdate = True

                self.__state = 1
                self.__nextState = 2
            elif self.__nextState == 2:
                self.__treeImg.undraw()
                self.__treeImg = Image(self.__treeImg.getAnchor(), "burn.png")
                self.__treeImg.draw(self.__win)
                needAnotherUpdate = True

                self.__state = 2
                self.__nextState = 3
            elif self.__nextState == 3:
                self.__treeImg.undraw()
                self.__treeImg = Image(self.__treeImg.getAnchor(), "charcoal.png")
                self.__treeImg.draw(self.__win)
                needAnotherUpdate = False

                self.__state = 3
                self.__nextState = 4
        elif self.__state == 3 or self.__nextState == 0:
            needAnotherUpdate = False

        return needAnotherUpdate
