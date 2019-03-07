# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab14 Functions 2
# 06 Mar 2019

# Import Packages
from graphics import *
from math import sqrt

# Initialize Constants
win = GraphWin('Lab 14: Functions 2', 400, 400)

# Define step1()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step1():
    # Call createButton()
    rect, text = createButton(25, 40, 75, 60, 'green', 'Click Me!', 24, 'white')

    # Call drawObject()
    drawObject(rect, text)

# Define createButton()
# Inputs:
#   int: x1
#   int: y1
#   int: x2
#   int: y2
#   str: background_clr
#   str: label
#   int: txt_size
#   str: txt_clr
# Outputs:
#   rectangle: rect
#   text: text
def createButton(x1, y1, x2, y2, background_clr, label, txt_size, txt_clr):
    # Sets rect and text as global variables because they are referenced in multiple steps
    global rect
    global text

    # Create the points
    pt1 = Point(x1, y1)
    pt2 = Point(x2, y2)

    # Create the rectangle, set its color
    rect = Rectangle(pt1, pt2)
    rect.setFill(background_clr)

    # Finds the location for the text
    text_ctr_x = x2 - x1
    text_ctr_y = y1 + ((y2 - y1) / 2)
    text_ctr = Point(text_ctr_x, text_ctr_y)

    # Create the text, set its color, size
    text = Text(text_ctr, label)
    text.setSize(txt_size)
    text.setFill(txt_clr)

    # Returns points
    return rect, text

# Define drawObject()
# Inputs:
#   graphics object: obj
#   text: text
# Outputs:
#   NONE
def drawObject(obj, text):
    # Draw the object and text on win
    obj.draw(win)
    text.draw(win)

# Define step2()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step2():
    # Call checkCllick()
    checkClick(rect)

    # When the button is clicked, set the color to red
    rect.setFill('red')

# Define clicked()
# Inputs:
#   rectangle: rect
#   mouse_click: click_pt
# Outputs:
#   bool: click
def clicked(rect, click_pt):
    # Gets the points cooresponding to the rectangle
    p1 = rect.getP1()
    p2 = rect.getP2()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()

    # Gets the points cooresponding to the click
    click_x = click_pt.getX()
    click_y = click_pt.getY()

    # Checks to see if the click is in the rectangle
    if (click_x >= p1_x and click_x <= p2_x) and \
       (click_y >= p1_y and click_y <= p2_y):
        click = True
    else:
        click = False

    # Returns whether the button is clicked or not
    return click

# Define checkClick()
# Inputs:
#   rectangle: rect
# Outputs:
#   NONE
def checkClick(rect):
    # Check to see if the button has been clicked
    clickPoint = win.getMouse()
    # Call clicked()
    click = clicked(rect, clickPoint)

    # Loops until the button is clicked
    while not click:
        click_pt = win.getMouse()
        click = clicked(rect, click_pt)

# Define step3()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step3():
    # Get two mouse clicks from the user and calculate the distance between
    click1 = win.getMouse()
    click2 = win.getMouse()
    # Call distance() and print the result
    print(distance(click1, click2))

# Define distance()
# Inputs:
#   point: p1
#   point: p2
# Outputs:
#   float: dist
def distance(p1, p2):
    # Gets x and y from p1 and p2
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()

    # Calculates the distance between p1 and p2
    dist = sqrt(((p2_x - p1_x) ** 2) + ((p2_y - p1_y) ** 2))

    # Returns the distance
    return dist

# Define step4()
# Inputs:
#   NONE
# Outputs:
#   NONE
def step4():
    # Call createCircle()
    circle, text = createCircle(50, 50, 20, 'green', 'Click Me Now!', 18, 'white')

    # Call drawObject()
    drawObject(circle, text)

    # Get clickPoint from user
    click_pt = win.getMouse()

    # Call checkClickInCircle()
    clicked = checkClickInCircle(circle, click_pt)

    # Loops until the user clicks the circle
    while not clicked:
        # Get clickPoint from user
        click_pt = win.getMouse()

        # Call checkClickInCircle()
        clicked = checkClickInCircle(circle, click_pt)

    # Once the circle is clicked, change the color
    circle.setFill('red')

# Define createCircle()
# Inputs:
#   int: x
#   int: y
#   int: r
#   str: background_clr
#   str: text
#   int: text_size
#   str: text_clr
# Outputs:
#   circle: circle
#   text: text
def createCircle(x, y, r, background_clr, text, text_size, text_clr):
    # Create the circle
    centre = Point(x, y)
    circle = Circle(centre, r)
    circle.setFill(background_clr)

    # Create the text
    text = Text(centre, text)
    text.setSize(text_size)
    text.setFill(text_clr)

    return circle, text

# Define checkClickInCircle()
# Inputs:
#   circle: circle
#   clickPoint: click_pt
# Outputs:
#   bool: clicked
def checkClickInCircle(circle, click_pt):
    # Get circle radius and center
    r = circle.getRadius()
    centre = circle.getCenter()

    # Get the distance between circle center and click_pt
    # Call distance()
    dist = distance(centre, click_pt)

    # Check to see if the click is in the circle
    if dist <= r:
        clicked = True
    else:
        clicked = False

    # Return the appropiate value
    return clicked

# Define main()
def main():
    # Set window coordinates and background
    win.setBackground('gray')
    win.setCoords(0, 0, 100, 100)

    # Call step1()
    step1()

    # Call step2()
    step2()

    # Call step3()
    step3()

    # Wait
    win.getMouse()

    # Remove the button from the screen
    rect.undraw()
    text.undraw()

    # Call step4()
    step4()

    # Wait
    win.getMouse()

    # Close the window
    win.close()

# Call main()
main()
