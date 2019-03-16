# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab05 Mastermind
# 15 Mar 2019
# Mastermind

# Import Packages
import random
from graphics import *
from math import sqrt

# Define genColors()
# Inputs:
#   NONE
# Outputs:
#   list: colors
def genColors():
    # Init colors
    colors = list()

    # Generate 4 colors randomly
    for i in range(4):
        # Randomly generate a number to represent the four colors
        clr_int = random.randint(1, 6)

        # Adds the color to colors
        colors.append(clr_int)

    return colors

# Define initWindow()
# Inputs:
#   NONE
# Outputs:
#   Window: win
def initWindow():
    # Create the window
    win = GraphWin('Mastermind', 400, 600)
    win.setCoords(0, 0, 100, 150)
    win.setBackground('white')

    # Draw 8 separator lines, 1 top line
    x1 = 0
    x2 = 100
    for i in range(1, 10):
        # Nine sections
        y = i * (150 / 9)

        # Points
        pt1 = Point(x1, y - 0.01)
        pt2 = Point(x2, y + 0.01)

        # Create and draw the lines
        rect = Rectangle(pt1, pt2)
        rect.draw(win)

    # Init the answer space
    answer = Text(Point(20, 141.6), 'Correct Answer:')
    answer.setSize(16)
    answer.draw(win)

    # Loop to draw 4 circles
    for i in range(1, 5):
        x = 40 + (12 * i)
        y = 141.6
        pt = Point(x, y)
        drawColorCircle(win, pt, 0)

    return win

# Define drawColorCircle()
# Inputs:
#   Window: win
#   Point: center
#   int: color_code
# Outputs:
#   Circle: circle
def drawColorCircle(win, center, color_code):
    # Create the circle
    circle = Circle(center, 5)

    # Decide the color and set the fill
    if color_code == 0:
        circle.setFill('white')
    elif color_code == 1:
        circle.setFill('blue')
    elif color_code == 2:
        circle.setFill('green')
    elif color_code == 3:
        circle.setFill('red')
    elif color_code == 4:
        circle.setFill('yellow')
    elif color_code == 5:
        circle.setFill('gray')
    elif color_code == 6:
        circle.setFill('brown')

    # Draw the circle
    circle.draw(win)

    return circle

# Define playGame()
# Inputs:
#   Window: win
#   list: solution
# Outputs:
#   bool: winner
def playGame(win, solution):
    # Init variables
    gameOver = False
    i = 1

    # Runs a loop for the game
    while not(gameOver):
        # Get the color input for the four colors
        # Call getUserColors()
        usr_clr = getUserColors(win, i)

        # Calculate the number of black and white circles
        # Call checkGuess()
        black, white = checkGuess(solution, usr_clr)

        # Call drawBlackWhiteCircles()
        drawBlackWhiteCircles(win, i, black, white)

        # If this is the eighth attempt or if the user enters the correct colors, end the game
        if usr_clr == solution:
            gameOver = True
            winner = True
        elif i == 8:
            gameOver = True
            winner = False

        # Update variables
        i += 1

    return winner

# Define getUserColors()
# Inputs:
#   Window: win
#   int: rnd
# Outputs:
#   list: guess
def getUserColors(win, rnd):
    # Determine coordinates for the button
    btn_x1 = 10
    btn_x2 = 30
    btn_y1 = 5.1 + (16.66 * (rnd - 1))
    btn_y2 = 11.5 + (16.66 * (rnd - 1))
    txt_x = 20
    txt_y = (btn_y1 + btn_y2) / 2

    # Create and draw the button
    btn = Rectangle(Point(btn_x1, btn_y1), Point(btn_x2, btn_y2))
    btn.setFill('lightgray')
    btn.draw(win)
    btnTxt = Text(Point(txt_x, txt_y), 'Check!')
    btnTxt.setSize(12)
    btnTxt.draw(win)

    # Draw the 4 circles
    circle_centers = list()
    for i in range(1, 5):
        x = 40 + (12 * i)
        y = txt_y
        pt = Point(x, y)
        drawColorCircle(win, pt, 0)

        # Save the centers for later reference
        circle_centers.append([pt, 0])

    # Now time to cycle through colors as the user clicks the circles
    # Init variables
    timeToCheck = False

    # Loop until the user is ready to check
    guess = [0, 0, 0, 0]
    while not(timeToCheck):
        # Get the click
        click = win.getMouse()
        click_center = None

        # Loop through each point and check distance between point and click
        circle_i = 0
        for point in circle_centers:
            if distance(point[0], click) <= 5:
                circle_center = point
                click_center = point[0]
                circle_reference = circle_i
            circle_i += 1

        # If the click was in a circle, skip this
        # Check to see if the click was within the button
        if click_center == None:
            if (click.getX() >= btn_x1 and click.getX() <= btn_x2) and \
               (click.getY() >= btn_y1 and click.getY() <= btn_y2) and \
               (0 not in guess):
                timeToCheck = True
        else:
            if circle_center[1] < 6:
                # Update the color in the list of the circles and update the button
                new_color = circle_center[1] + 1
                circle_centers[circle_reference][1] = new_color
                drawColorCircle(win, click_center, new_color)

                # Update the list of colors to return
                guess[circle_reference] = new_color
            else:
                # Update the color in the list of the circles and update the button
                circle_centers[circle_reference][1] = 1
                drawColorCircle(win, click_center, 1)

                # Update the list of colors to return
                guess[circle_reference] = 1

    # Undraw button for black and white circles
    btn.undraw()
    btnTxt.undraw()

    return guess

# Define distance()
# Inputs:
#   Point: ref_pt
#   Point: click_pt
# Outputs:
#   float: dist
def distance(ref_pt, click_pt):
    # Get variables
    x1 = ref_pt.getX()
    y1 = ref_pt.getY()
    x2 = click_pt.getX()
    y2 = click_pt.getY()

    # Calculate distance
    dist = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    return dist

# Define checkGuess()
# Inputs:
#   list: solution
#   list: guess
# Outputs:
#   int: black_circle
#   int: white_circle
def checkGuess(solution, guess):
    # Init variables
    guess_wpos = list()
    solution_wpos = list()
    blacks_total = 0
    whites_total = 0

    # Add the position to elements for checking
    i = 0
    for g in guess:
        guess_wpos.append([i, g, 0, 0])
        i += 1

    j = 0
    for s in solution:
        solution_wpos.append([j, s, 0, 0])
        j += 1

    # Check to see if it should be a black or white circle by checking the position and value
    for g in guess_wpos:
        for s in solution_wpos:
            # If the position AND colors are the same, make a black circle
            if g[0] == s[0] and g[1] == s[1]:
                blacks_total += 1
                # 10 in the 2 position means there is a black circle for that value
                s[2] = 10
            # If the colors are the same and there isn't already a black circle, add a white circle
            elif g[1] == s[1] and s[2] != 10 and s[3] != 10:
                whites_total += 1
                # 10 in the 3 position means there is a white circle for that value
                s[3] = 10

    # If there is a black and white circle for a guess, remove the white circle
    for s in solution_wpos:
        if s[2] == 10 and s[3] == 10:
            whites_total -= 1

    return blacks_total, whites_total

# Define drawBlackWhiteCircles()
# Inputs:
#   Window: win
#   int: rnd
#   int: black_circle
#   int: white_circle
# Outputs:
#   NONE
def drawBlackWhiteCircles(win, rnd, black_circle, white_circle):
    # Finds the point for the center of the circles
    y1 = 5.1 + (16.66 * (rnd - 1))
    y2 = 11.5 + (16.66 * (rnd - 1))
    x = 20
    y = (y1 + y2) / 2

    # Create the circles and puts them in a list
    cir1 = Circle(Point(x - 4, y + 4), 2)
    cir2 = Circle(Point(x + 4, y + 4), 2)
    cir3 = Circle(Point(x - 4, y - 4), 2)
    cir4 = Circle(Point(x + 4, y - 4), 2)

    circles = [cir1, cir2, cir3, cir4]

    # Loops through black and then white to draw circles
    circle_to_choose = 0
    i = 0
    while i < black_circle:
        cir = circles[circle_to_choose]
        cir.setFill('black')
        cir.draw(win)

        i += 1
        circle_to_choose += 1

    j = 0
    while j < white_circle:
        cir = circles[circle_to_choose]
        cir.setFill('white')
        cir.draw(win)

        j += 1
        circle_to_choose += 1

# Define displaySolution()
# Inputs:
#   Window: win
#   list: solution
# Outputs:
#   NONE
def displaySolution(win, solution):
    # Init variables
    i = 1

    # Loop through each number in the solution and draw a circle as appropiate
    for s in solution:
        x = 40 + (12 * i)
        y = 141.6
        pt = Point(x, y)
        drawColorCircle(win, pt, s)

        # Update variables
        i += 1

# Define playerWon()
# Inputs:
#   Window: win
# Outputs:
#   NONE
def playerWon(win):
    rect = Rectangle(Point(20, 80), Point(75, 85))
    rect.setFill('lightgray')
    rect.draw(win)

    textBox = Text(Point(50, 80), 'Congrats, you won!')
    textBox.setSize(16)
    textBox.draw(win)

    textBox2 = Text(Point(50, 70), 'Click anywhere to close.')
    textBox2.setSize(10)
    textBox2.setStyle('italic')
    textBox2.draw(win)

# Define playerWon()
# Inputs:
#   Window: win
# Outputs:
#   NONE
def playerLost(win):
    rect = Rectangle(Point(20, 65), Point(80, 85))
    rect.setFill('lightgray')
    rect.draw(win)

    textBox = Text(Point(50, 80), 'I\'m sorry, but you lost.')
    textBox.setSize(16)
    textBox.draw(win)

    textBox2 = Text(Point(50, 70), 'Click anywhere to close.')
    textBox2.setSize(10)
    textBox2.setStyle('italic')
    textBox2.draw(win)

# Define main()
def main():
    # Randomly generate the six colors for the answer
    clr_solution = genColors()

    # Call initWindow()
    win = initWindow()
    
    # Play the game
    winner = playGame(win, clr_solution)

    # Call displaySolution()
    displaySolution(win, clr_solution)

    if winner:
        # Call playerWon()
        playerWon(win)
    else:
        # Call playerLost()
        playerLost(win)

    # Wait
    win.getMouse()

# Call main()
main()
