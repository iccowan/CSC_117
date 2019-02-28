# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab12 Graphics - Bouncing DVD Logo
# 27 Feb 2019

# Import Packages
from graphics import *
import random

# Open the window
win = GraphWin('DVD Bouncing', 640, 360)
win.setBackground('black')
win.setCoords(0, 0, 640, 360)

# Draw the DVD logo
dvd = Image(Point(320, 180), 'white-dvd.png')
dvd.draw(win)

# Randomly chooses a direction to begin
direction = random.randint(1, 4)

# Loop runs until the video beings "playing"
playing = False
change_direction = False
while not playing:
    if direction == 1:
        dvd.move(1, 1)
    elif direction == 2:
        dvd.move(1, -1)
    elif direction == 3:
        dvd.move(-1, -1)
    elif direction == 4:
        dvd.move(-1, 1)

    # Gets the location of the DVD logo
    center = dvd.getAnchor()
    width = dvd.getWidth()
    height = dvd.getHeight()
    time.sleep(0.05)

    # Determines the four corners of the DVD logo
    top_right = Point(center.getX() + (width / 2), center.getY() + (height / 2))
    top_left = Point(center.getX() - (width / 2), center.getY() + (height / 2))
    bottom_left = Point(center.getX() - (width / 2), center.getY() - (height / 2))
    bottom_right = Point(center.getX() + (width / 2), center.getY() - (height / 2))

    # Determines if the DVD logo is at one of the corners
    # If so, change_direction is set to true
    if (top_right.getY() >= 360 or top_left.getY() >= 360) or \
       (top_right.getX() >= 640 or top_left.getX() <= 0) or \
       (bottom_left.getY() <= 0 or bottom_right.getY() <= 0) or \
       (bottom_left.getX() <= 0 or bottom_right.getX() >= 640):
        change_direction = True

    # If it needs to change direction, it does so and repeats until it's a new direction
    if change_direction:
        last_direction = direction
        direction = random.randint(1, 4)

        # Prevents the logo from going back in the same direction
        while (direction == 1 and last_direction == 3) or \
              (direction == 3 and last_direction == 1) or \
              (direction == 2 and last_direction == 4) or \
              (direction == 4 and last_direction == 2):
            direction = random.randint(1, 4)

        # Prevents the logo from going off the screen
        if direction == 1:
            # dvd.move(1, 1)
            n_top_right = Point(top_right.getX() + 1, top_right.getY() + 1)
            n_top_left = Point(top_left.getX() + 1, top_left.getY() + 1)
            n_bottom_left = Point(bottom_left.getX() + 1, bottom_left.getY() + 1)
            n_bottom_right = Point(bottom_right.getX() + 1, bottom_right.getY() + 1)
        elif direction == 2:
            # dvd.move(1, -1)
            n_top_right = Point(top_right.getX() + 1, top_right.getY() - 1)
            n_top_left = Point(top_left.getX() + 1, top_left.getY() - 1)
            n_bottom_left = Point(bottom_left.getX() + 1, bottom_left.getY() - 1)
            n_bottom_right = Point(bottom_right.getX() + 1, bottom_right.getY() - 1)
        elif direction == 3:
            # dvd.move(-1, -1)
            n_top_right = Point(top_right.getX() - 1, top_right.getY() - 1)
            n_top_left = Point(top_left.getX() - 1, top_left.getY() - 1)
            n_bottom_left = Point(bottom_left.getX() - 1, bottom_left.getY() - 1)
            n_bottom_right = Point(bottom_right.getX() - 1, bottom_right.getY() - 1)
        elif direction == 4:
            # dvd.move(-1, 1)
            n_top_right = Point(top_right.getX() - 1, top_right.getY() + 1)
            n_top_left = Point(top_left.getX() - 1, top_left.getY() + 1)
            n_bottom_left = Point(bottom_left.getX() - 1, bottom_left.getY() + 1)
            n_bottom_right = Point(bottom_right.getX() - 1, bottom_right.getY() + 1)

        # If the logo is going to go off the screen, a loop will begin to prevent it from doing so
        while (n_top_right.getY() >= 360 or n_top_left.getY() >= 360) or \
              (n_top_right.getX() >= 640 or n_top_left.getX() <= 0) or \
              (n_bottom_left.getY() <= 0 or n_bottom_right.getY() <= 0) or \
              (n_bottom_left.getX() <= 0 or n_bottom_right.getX() >= 640):
            direction = random.randint(1, 4)

            # Prevents the logo from going back in the opposite direction
            while (direction == 1 and last_direction == 3) or \
                  (direction == 3 and last_direction == 1) or \
                  (direction == 2 and last_direction == 4) or \
                  (direction == 4 and last_direction == 2):
                direction = random.randint(1, 4)

            # Again prevents the logo from going off the screen
            if direction == 1:
                # dvd.move(1, 1)
                n_top_right = Point(top_right.getX() + 1, top_right.getY() + 1)
                n_top_left = Point(top_left.getX() + 1, top_left.getY() + 1)
                n_bottom_left = Point(bottom_left.getX() + 1, bottom_left.getY() + 1)
                n_bottom_right = Point(bottom_right.getX() + 1, bottom_right.getY() + 1)
            elif direction == 2:
                # dvd.move(1, -1)
                n_top_right = Point(top_right.getX() + 1, top_right.getY() - 1)
                n_top_left = Point(top_left.getX() + 1, top_left.getY() - 1)
                n_bottom_left = Point(bottom_left.getX() + 1, bottom_left.getY() - 1)
                n_bottom_right = Point(bottom_right.getX() + 1, bottom_right.getY() - 1)
            elif direction == 3:
                # dvd.move(-1, -1)
                n_top_right = Point(top_right.getX() - 1, top_right.getY() - 1)
                n_top_left = Point(top_left.getX() - 1, top_left.getY() - 1)
                n_bottom_left = Point(bottom_left.getX() - 1, bottom_left.getY() - 1)
                n_bottom_right = Point(bottom_right.getX() - 1, bottom_right.getY() - 1)
            elif direction == 4:
                # dvd.move(-1, 1)
                n_top_right = Point(top_right.getX() - 1, top_right.getY() + 1)
                n_top_left = Point(top_left.getX() - 1, top_left.getY() + 1)
                n_bottom_left = Point(bottom_left.getX() - 1, bottom_left.getY() + 1)
                n_bottom_right = Point(bottom_right.getX() - 1, bottom_right.getY() + 1)

        # Sets the change_direction to false to prevent random direction changes
        change_direction = False
