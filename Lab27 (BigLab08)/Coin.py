# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab08 Coins
# 19 Apr 2019
# COIN CLASS

# Import Dependencies
from graphics import *
from math import sqrt

# Attributes:
#   Window __win
#   Circle __circle
#   int __sideUp
#   boolean __isClose
# Methods:
#   void .flip()
#   list<boolean> .clicked(Point)
class Coin:
    def __init__(self, window, center, isClose):
        self.__win = window
        self.__circle = Circle(center, 4)

        # The closing circle will be red
        if isClose:
            self.__circle.setFill("red")

            # Put an X in the close coin
            t = Text(center, "X")
            t.setSize(16)
        else:
            self.__circle.setFill("blue")
        
        self.__sideUp = 0
        self.__isClose = isClose

        # Draw the coin
        self.__circle.draw(self.__win)

        # Draw the text if it's the closing coin
        if isClose:
            t.draw(window)

    def flip(self):
        if self.__sideUp == 1:
           self.__sideUp = 0
           self.__circle.setFill("blue")
        else:
            self.__sideUp = 1
            self.__circle.setFill("yellow")

    def isCoinClose(self):
        return self.__isClose

    def clicked(self, clickpt):
        circleCenter = self.__circle.getCenter()
        
        # Get x's and y's
        x1 = circleCenter.getX()
        x2 = clickpt.getX()
        y1 = circleCenter.getY()
        y2 = clickpt.getY()

        # Check and see if the click was inside of the circle
        if calcDistance(x1, x2, y1, y2) <= 4:
            clicked = True
        else:
            clicked = False

        # Check and see if the coin is the closing coin
        if clicked and self.__isClose:
            self.__win.close()
            winClosed = True
        else:
            winClosed = False

        return [clicked, winClosed]

# Define calcDistance()
# Inputs:
#   float x1
#   float x2
#   float y1
#   float y2
# Ouputs:
#   float d
def calcDistance(x1, x2, y1, y2):
    # Calculate the distance
    d = sqrt(((x1 - x2) ** 2) + ((y1 - y2) **2))
    return d
