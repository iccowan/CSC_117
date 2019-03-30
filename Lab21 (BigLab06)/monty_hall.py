# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab06 Monty Hall
# 29 Mar 2019
# Let's Make a Deal Monty Hall

# Import Packages
from graphics import *
import random

# Define initWindow()
# Inputs:
#   NONE
# Outputs:
#   Window: win
def initWindow():
    # Open up the window
    win = GraphWin('Let\'s Make a Deal: Monty Hall', 1000, 500)
    win.setCoords(0, 0, 200, 100)
    win.setBackground('green')

    # Create the 'click a door'
    txt = createText('Click a Door', 14, Point(100, 95), 'black')
    txt.draw(win)

    # Draw the 3 buttons
    createButton(win, 'Switch', 'black', 'white', Point(50, 50))
    createButton(win, 'Stay', 'black', 'white', Point(100, 50))
    createButton(win, 'Play Again', 'black', 'white', Point(150, 50))

    # Create the text areas for total times won/lost
    staylose = createText('Times Stayed & Lost:', 10, Point(15, 2), 'black')
    staywin = createText('Times Stayed & Won:', 10, Point(15, 6), 'black')
    changelose = createText('Times Changed & Lost:', 10, Point(15, 10), 'black')
    changewin = createText('Times Changed & Won:', 10, Point(15, 14), 'black')
    staylose.draw(win)
    staywin.draw(win)
    changelose.draw(win)
    changewin.draw(win)

    return win

# Define createText():
# Inputs:
#   str: txt
#   int: txt_size
#   Point: ref_pt
#   str: fill
# Outputs:
#   Text: txt_object
def createText(txt, txt_size, ref_pt, fill):
    # Create the text object with color and size and all
    txt_object = Text(ref_pt, txt)
    txt_object.setSize(txt_size)
    txt_object.setFill(fill)

    return txt_object

# Define createButton()
# Inputs:
#   Window: win
#   str: txt
#   str: outline
#   str: fill
#   Point: ref_pt
def createButton(win, txt, outline, fill, ref_pt):
    # Find the points for the rectangle(s)
    x1 = ref_pt.getX() - 15
    x2 = ref_pt.getX() + 15
    y1 = ref_pt.getY() - 5
    y2 = ref_pt.getY() + 5

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    # Create the rectangle
    rect = Rectangle(p1, p2)
    rect.setFill(fill)
    rect.setWidth(3)
    rect.setOutline(outline)

    # Create the text label
    label = Text(ref_pt, txt)
    label.setSize(14)

    # Draw the button
    rect.draw(win)
    label.draw(win)

# Define playGame()
# Inputs:
#   Window: win
# Outputs:
#   NONE
def playGame(win):
    # Init variables
    gameOver = False
    switch_win = 0
    switch_lose = 0
    stay_win = 0
    stay_lose = 0
    counts = list()
    border = Rectangle(Point(35, 45), Point(65, 55))
    border.setWidth(3)
    border.setOutline('black')
    border.draw(win)
    desc = createText('Placeholder for loop', 10, Point(150, 20), 'green')
    desc.draw(win)

    # Call drawCount()
    counts = drawCount(win, counts, switch_win, switch_lose, stay_win, stay_lose)

    # Run the game until it's over
    while not gameOver:
        # Init variables that should change each run
        zonk_doors, win_door = pickDoors()
        border.undraw()
        desc.undraw()

        # Let the user choose a door to begin
        door_choice = pickDoor(win)

        # Open a zonk door that is not the user's choice or winning door
        dto = random.randint(1, 3)
        while dto == door_choice or dto == win_door:
            dto = random.randint(1, 3)

        # Open the dto
        openDoor(win, dto, True)

        # Check to see if the user wants to change their door or keep it
        switch = userChangeDoor(win)

        # Make sure the user has clicked a button
        while switch == None:
            switch = userChangeDoor(win)

        # If the user wants to switch, switch the door
        if switch:
            new_door = random.randint(1, 3)
            while new_door == dto or new_door == door_choice:
                new_door = random.randint(1, 3)

            door_choice = new_door

            # Draw a new border around the selected button
            border = Rectangle(Point(35, 45), Point(65, 55))
            border.setWidth(3)
            border.setOutline('blue')
            border.draw(win)
        else:
            # Draw a new border around the selected button
            border = Rectangle(Point(85, 45), Point(115, 55))
            border.setWidth(3)
            border.setOutline('blue')
            border.draw(win)

        # Check to see if the user's door is a zonk
        if door_choice == win_door:
            winner = True
        else:
            winner = False

        # Open the other 2 doors
        dto_l = random.randint(1, 3)
        while dto_l == dto or dto_l == win_door:
            dto_l = random.randint(1, 3)

        openDoor(win, dto_l, True)
        openDoor(win, win_door, False)

        # Update variables and put a description
        if winner and switch:
            desc = createText('Congratulations, you switched and won!', 18, Point(120, 25), 'blue')
            switch_win += 1
        elif (not winner) and switch:
            desc = createText('ZONK! You switched and lost!', 18, Point(120, 25), 'blue')
            switch_lose += 1
        elif winner and (not switch):
            desc = createText('Congratulations, you stayed and won!', 18, Point(120, 25), 'blue')
            stay_win += 1
        elif (not winner) and (not switch):
            desc = createText('ZONK! You stayed and lost!', 18, Point(120, 25), 'blue')
            stay_lose += 1

        # Draw the desc
        desc.draw(win)

        # Call drawCount()
        counts = drawCount(win, counts, switch_win, switch_lose, stay_win, stay_lose)

        # Ask the user if they want to play again
        gameOver = playAgain(win)

# Define drawCount()
# Inputs:
#   Window: win
#   list: old_counts
#   int: switch_win
#   int: switch_lose
#   int: stay_win
#   int: stay_lose
# Outputs:
#   list: counts
def drawCount(win, old_counts, switch_win, switch_lose, stay_win, stay_lose):
    # Undraws old counts
    for c in old_counts:
        c.undraw()

    # Draws all of the counts and adds them to the list
    stl_txt = createText(str(stay_lose), 10, Point(32, 2), 'black')
    stw_txt = createText(str(stay_win), 10, Point(32, 6), 'black')
    chl_txt = createText(str(switch_lose), 10, Point(32, 10), 'black')
    chw_txt = createText(str(switch_win), 10, Point(32, 14), 'black')
    stl_txt.draw(win)
    stw_txt.draw(win)
    chl_txt.draw(win)
    chw_txt.draw(win)

    # Put all of them into a list
    counts = [stl_txt, stw_txt, chl_txt, chw_txt]

    return counts

# Define pickDoors()
# Inputs:
#   NONE
# Outputs:
#   list: zonk_doors
#   int: win_door
def pickDoors():
    # Randomly choose the 2 zonk doors
    zonk_door1 = random.randint(1,3)
    zonk_door2 = random.randint(1,3)

    # Make sure we have 2 different doors
    while zonk_door1 == zonk_door2:
        zonk_door2 = random.randint(1, 3)

    # Add the zonk doors to a list
    zonk_doors = [zonk_door1, zonk_door2]

    # Decide which door is a winner
    if 1 in zonk_doors and 2 in zonk_doors:
        win_door = 3
    elif 1 in zonk_doors and 3 in zonk_doors:
        win_door = 2
    elif 2 in zonk_doors and 3 in zonk_doors:
        win_door = 1

    return zonk_doors, win_door

# Define pickDoor()
# Inputs:
#   Window: win
# Outputs:
#   int: door
def pickDoor(win):
    # Draw the doors to choose from
    door1 = Image(Point(50, 80), 'door1.png')
    door2 = Image(Point(100, 80), 'door2.png')
    door3 = Image(Point(150, 80), 'door3.png')
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    # Call checkIfInsideButton()
    inside, door = checkIfInsideButton(win)

    # Wait until the user clicks a door
    while not inside:
        inside, door = checkIfInsideButton(win)

    return door

# Define checkIfInsideButton()
# Inputs:
#   Window: win
# Outputs:
#   bool: inside
#   int: door
def checkIfInsideButton(win):
    # Get the user's click
    click_pt = win.getMouse()

    # Check to see if the click is inside a box
    if click_pt.getX() >= 37.5 and click_pt.getX() <= 62.5 and \
       click_pt.getY() >= 70.6 and click_pt.getY() <= 89.6:
        inside = True
        door = 1
    elif click_pt.getX() >= 87.5 and click_pt.getX() <= 112.5 and \
         click_pt.getY() >= 70.6 and click_pt.getY() <= 89.6:
        inside = True
        door = 2
    elif click_pt.getX() >= 137.5 and click_pt.getX() <= 162.5 and \
         click_pt.getY() >= 70.6 and click_pt.getY() <= 89.6:
        inside = True
        door = 3
    else:
        inside = False
        door = 0

    return inside, door

# Define openDoor()
# Inputs:
#   Window: win
#   int: door
#   bool: zonk
# Outputs:
#   NONE
def openDoor(win, door, zonk):
    # Check for the door type
    if zonk:
        img = 'zonk.png'
    else:
        img = 'ferrari.png'

    # Decide the door and draw the door
    if door == 1:
        door_img = Image(Point(50, 80), img)
    elif door == 2:
        door_img = Image(Point(100, 80), img)
    elif door == 3:
        door_img = Image(Point(150, 80), img)

    # Draw the zonk
    door_img.draw(win)

# Define userChangeDoor()
# Inputs:
#   Window: win
# Outputs:
#   bool: want_change
def userChangeDoor(win):
    # Init variables
    want_change = None

    # Get the user's click
    click_pt = win.getMouse()

    # Check the click
    if click_pt.getX() >= 35 and click_pt.getX() <= 65 and \
       click_pt.getY() >= 45 and click_pt.getY() <= 55:
        want_change = True
    elif click_pt.getX() >= 85 and click_pt.getX() <= 115 and \
         click_pt.getY() >= 45 and click_pt.getY() <= 55:
        want_change = False

    return want_change

# Define playAgain()
# Inputs:
#   Window: win
# Outputs:
#   bool: finished
def playAgain(win):
    # Get the user's click
    click_pt = win.getMouse()

    # Check to see if the click is inside the button
    if click_pt.getX() >= 135 and click_pt.getX() <= 165 and \
       click_pt.getY() >= 45 and click_pt.getY() <= 55:
        finished = False
    else:
        finished = True

    return finished

# Define main()
def main():
    # Call initWindow()
    win = initWindow()

    # Call playGame()
    playGame(win)

# Call main()
main()
