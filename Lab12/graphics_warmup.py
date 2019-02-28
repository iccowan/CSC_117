# Ian Cowan
# CSC 117b Lab12 Graphics Warmup
# 27 Feb 2019

# Import Packages
from graphics import *
import time

# Graphics warmup!
print('Graphics warmup!')

# Set parameters of graphics window
windowWidth = 400
windowHeight = 400
windowTitle = 'My Cool Window'

# Create the window by instantiating the GraphWin class and set the coordinates
print('Creating graphics window...')
win = GraphWin(windowTitle, windowWidth, windowHeight)
win.setCoords(0, 0, 100, 100)

# Draw a circle
centre = Point(10, 50)
myCircle = Circle(centre, 10)
myCircle.setFill('black')
# myCircle.draw(win)
dvd = Image(centre, 'dvd.png')
dvd.draw(win)

# Bounce back and fourth until the user clicks
print('Click the screen to stop the ball...')
done = False
while not done:
    # Make the circle move right
    count = 80
    while count > 0:
        if not done:
            dvd.move(1, 0)
            time.sleep(0.05)
            clickPoint = win.checkMouse()
            if clickPoint:
                done = True
                count = 0
            count += -1

    # Make the circle move left
    count = 80
    if not done:
        while count > 0:
            dvd.move(-1, 0)
            time.sleep(0.05)
            clickPoint = win.checkMouse()
            if clickPoint:
                done = True
                count = 0
            count += -1

    # Check for the user clicking the mouse
    clickPoint = win.checkMouse()
    if clickPoint:
        done = True

# Make the circle disappear
print('Click anywhere to make the circle disappear...')
win.getMouse()
dvd.undraw()

# Wait until the user clicks the mouse before closing the window
print('Click anywhere to end the program...')
win.getMouse()
win.close()

# Tells the user (assuming the user is a human) goodbye
print('Goodbye, human!')
