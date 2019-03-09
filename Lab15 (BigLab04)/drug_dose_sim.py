# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b BigLab04 Drug Dose Simulator
# 8 Mar 2019
# Drug Dose Simulator

# Import Packages
from graphics import *
import time

# Define validateDoseInputs()
# Inputs:
#   float: lethaldose
#   float: overdose
#   float: effectivedose
# Outputs:
#   float: lethaldose
#   float: overdose
#   float: effectivedose
def validateDoseInputs(lethaldose, overdose, effectivedose):
    # Make sure the effective dose is less than the overdose
    while not(effectivedose <= overdose):
        print('The effective dose must be less than the overdose')
        overdose = float(input('How many mg of the drug is considered an overdose? '))
        effectivedose = float(input('How many mg of the drug is considered effective? '))

    # Make sure the overdose is less than the lethaldose
    while not(overdose <= lethaldose):
        print('The overdose must be less than the lethal dose')
        lethaldose = float(input('How many mg of the drug is lethal? '))
        overdose = float(input('How many mg of the drug is considered an overdose? '))

    # Make sure the values are all 0-100mg
    while not(effectivedose >= 0 and effectivedose <= 100):
        print('The doses must be positive but less than 100mg')
        effectivedose = float(input('How many mg of the drug is considered effective? '))

    while not(overdose >= 0 and overdose <= 100):
        print('The doses must be positive but less than 100mg')
        overdose = float(input('How many mg of the drug is considered an overdose? '))

    while not(lethaldose >= 0 and lethaldose <= 100):
        print('The doses must be positive but less than 100mg')
        lethaldose = float(input('How many mg of the drug is lethal? '))

    return lethaldose, overdose, effectivedose

# Define validateDecayRate()
# Inputs:
#   float: decayrate
# Outputs:
#   float: decayrate
def validateDecayRate(decayrate):
    while not(decayrate >= 0):
        print('The decay rate should not be less than zero percent')
        decayrate = float(input('What percentage of the drug should decay every eight hours? '))

    # Return decayrate
    return decayrate

# Define runSimulation()
# Inputs:
#   float: lethaldose
#   float: overdose
#   float: effectivedose
#   float: decayrate
# Outputs:
#   Window: win
def runSimulation(lethaldose, overdose, effectivedose, decayrate):
    # Call initDisplay()
    win, btn, origin = initDisplay(lethaldose, overdose, effectivedose)

    # Wait for the button to be clicked to begin
    # Call waitForClick()
    waitForClick(win, btn)

    # Update the button
    btn = createButton(win, Point(150, 10), Point(170, 15), 'Try Next Dosage', 'gray', 'black')

    # Run the simulation 10 times
    for dose_mg in range(1, 11):
        # Call dosageSimulation()
        final_dose, effective_hr, overdose_hr, lethal_hr = dosageSimulation(win, dose_mg, decayrate, effectivedose, overdose, lethaldose, origin)

        # Call displaySimulationInfo()
        displaySimulationInfo(win, dose_mg, final_dose, effective_hr, overdose_hr, lethal_hr)

        # Only wait and clear if the simulation is not over
        if dose_mg < 10:
            # PAUSE...WAIT FOR CLICK
            # Call waitForClick()
            waitForClick(win, btn)

            # Call clearGraph()
            clearGraph(win, Point(150, 50), effectivedose, overdose, lethaldose, 100)

    return win

# Define initDisplay()
# Inputs:
#   float: lethaldose
#   float: overdose
#   float: effectivedose
# Outputs:
#   Window: win
#   Rectangle: btn
#   Point: origin
def initDisplay(lethaldose, overdose, effectivedose):
    # Create the window
    win = GraphWin('Drug Dosage Simulation', 1300, 650)

    # Set the coordinates in the window
    win.setCoords(0, 0, 200, 100)

    # Set the background color of the window
    win.setBackground('lightgray')

    # Create text boxes and draw them
    createText(Point(30, 75), 'Dosage (mg every 8 hours):', 'black').draw(win)

    # Call createGraph()
    origin, effective_y, overdose_y, lethal_y = createGraph(win, Point(150, 50), 0, 168, 8, 0, 100, 10, effectivedose, overdose, lethaldose)

    # Create the line to separate top and bottom portions
    line_rect = Rectangle(Point(0, 24.8), Point(200, 25.2))
    line_rect.setFill('black')
    line_rect.draw(win)

    # Create button for bottom portion
    btn = createButton(win, Point(150, 10), Point(170, 15), 'Begin Simulation', 'gray', 'black')

    return win, btn, origin

# Define createText()
# Inputs:
#   Point: pt
#   str: text
#   str: color
# Outputs:
#   Text: txt
def createText(pt, text, color):
    # Creates txt
    txt = Text(pt, text)
    txt.setFill(color)
    txt.setSize(10)

    # Returns the txt object
    return txt

# Define createGraph()
# Inputs:
#   Window: win
#   Point: pt
#   int: x_min
#   int: x_max
#   int: x_int
#   int: y_min
#   int: y_max
#   int: y_int
#   float: effective
#   float: over
#   float: lethal
# Outputs:
#   Point: origin
#   float: effective_center
#   float: over_center
#   float: lethal_center
def createGraph(win, pt, x_min, x_max, x_int, y_min, y_max, y_int, effective, over, lethal):
    # Call clearGraph()
    effective_center, over_center, lethal_center = clearGraph(win, pt, effective, over, lethal, y_max)

    # Label the axes
    createText(Point(100, 60), 'Drug in Body (mg)', 'black').draw(win)
    createText(Point(150, 30), 'Hour', 'black').draw(win)

    # Create the numbers at the desired interval on the x-axis
    x_point = pt.getX() - 34
    num_x = x_max / x_int + 1
    x_space = ((pt.getX() + 45) - (pt.getX() - 35)) / num_x

    # Create the numbers at the desired interval on the y-axis
    y_point = pt.getY() - 14
    num_y = y_max / y_int
    y_space = ((pt.getY() + 40) - (pt.getY() - 15)) / num_y

    # Create origin for future use
    origin = Point(x_point, y_point)

    # Loops through each number in the x interval
    for i in range(x_min, x_max + 1, x_int):
        txt_pt = Point(x_point, pt.getY() - 17)
        createText(txt_pt, str(i), 'black').draw(win)
        x_point += x_space

    # Loops through each number in the y interval
    for i in range(y_min, y_max + 1, y_int):
        txt_pt = Point(pt.getX() - 37, y_point)
        createText(txt_pt, str(i), 'black').draw(win)
        y_point += y_space

    # Label the lines
    createText(Point(pt.getX() + 47, effective_center), 'E', 'green').draw(win)
    createText(Point(pt.getX() + 47, over_center), 'O', 'yellow').draw(win)
    createText(Point(pt.getX() + 47, lethal_center), 'L', 'red').draw(win)

    # Returns the y-values for effective, overdose, and lethal
    return origin, effective_center, over_center, lethal_center

# Define clearGraph()
# Inputs:
#   Window: win
#   Point: pt
#   float: effective
#   float: over
#   float: lethal
#   int: y_max
# Outputs:
#   float: effective_center
#   float: over_center
#   float: lethal_center
def clearGraph(win, pt, effective, over, lethal, y_max):
    # Create a rectangular box at the reference point
    p1 = Point(pt.getX() - 35, pt.getY() - 15)
    p2 = Point(pt.getX() + 45, pt.getY() + 40)
    rect = Rectangle(p1, p2)
    rect.setFill('white')
    rect.draw(win)

    # Draws the lines on the graph for effective dose, overdose, and lethal dose using drawLine()
    # Effective dose
    effective_center = drawLine(win, y_max, pt, effective, 'green')
    over_center = drawLine(win, y_max, pt, over, 'yellow')
    lethal_center = drawLine(win, y_max, pt, lethal, 'red')

    return effective_center, over_center, lethal_center

# Define drawLine()
# Inputs:
#   Window: win
#   float: y_max
#   Point: pt
#   int: y_coord
#   str: color
# Outputs:
#   float: center_y
def drawLine(win, y_max, pt, y_coord, color):
    # Draws a line on the graph (written for effective and then transferred...working variables left alone)
    y_per_one = ((pt.getY() + 40) - (pt.getY() - 15)) / y_max
    effective_y = (pt.getY() - 15) + (y_per_one * y_coord)
    effective_ref = Point(pt.getX() - 35, effective_y + 1)
    effective_p1 = Point(effective_ref.getX(), effective_ref.getY() - 0.2)
    effective_p2 = Point(effective_ref.getX() + 80, effective_ref.getY() + 0.2)
    effective_rect = Rectangle(effective_p1, effective_p2)
    effective_rect.setFill(color)
    effective_rect.draw(win)

    # Finds the center y-value to return
    center_y = effective_ref.getY()

    # Returns the center y-value
    return center_y

# Define createButton()
# Inputs:
#   Window: win
#   Point: pt1
#   Point: pt2
#   str: text
#   str: back_clr
#   str: txt_clr
# Outputs:
#   Rectangle: button
def createButton(win, pt1, pt2, text, back_clr, txt_clr):
    # Create the rectangle
    button = Rectangle(pt1, pt2)
    button.setFill(back_clr)
    button.setOutline('black')

    # Get the reference coordinates for the text
    txt_x = (pt1.getX() + pt2.getX()) / 2
    txt_y = (pt1.getY() + pt2.getY()) / 2
    txt_ctr = Point(txt_x, txt_y)

    # Create the text
    txt = createText(txt_ctr, text, txt_clr)

    # Draw the button
    button.draw(win)
    txt.draw(win)

    return button

# Define waitForClick()
# Inputs:
#   Window: win
#   Rectangle: btn
# Outputs:
#   NONE
def waitForClick(win, btn):
    # Loops until clicked
    btn_clicked = checkForButtonClick(win, btn)
    while not (btn_clicked):
        btn_clicked = checkForButtonClick(win, btn)

# Define dosageSimulation()
# Inputs:
#   Window: win
#   float: dose_mg
#   float: decay
#   float: effective
#   float: overdose
#   float: lethal
#   Point: origin
# Outputs:
#   float: total_current_dose
#   int: effective_hr
#   int: overdose_hr
#   int: lethal_hr
def dosageSimulation(win, dose_mg, decay, effective, overdose, lethal, origin):
    # Initialize variables
    total_current_dose = 0
    effective_hr = None
    overdose_hr = None
    lethal_hr = None
    i = 0

    # Run the simulation 21 times for every 8 hours in the order:
    #   -> Decays the appropiate amount
    #   -> Adds the new dosage
    #   -> Checks for effective/overdose/death
    while i <= 21 and lethal_hr == None:
        # Decays the appropiate amount
        total_current_dose -= total_current_dose * (decay / 100)

        # Adds the new dosage
        total_current_dose += dose_mg

        # Checks for effective/overdose/death
        if (total_current_dose >= effective) and (effective_hr == None):
            effective_hr = i
        if (total_current_dose >= overdose) and (overdose_hr == None):
            overdose_hr = i
        if (total_current_dose >= lethal) and (lethal_hr == None):
            lethal_hr = i

        # Call displayHourlyInfo()
        displayHourlyInfo(win, total_current_dose, origin, i)

        i += 1

        # Slow down the simulation so it does not seem instantaneous
        time.sleep(0.5)

    # Returns all of the applicable information
    return total_current_dose, effective_hr, overdose_hr, lethal_hr

# Define displayHourlyInfo()
# Inputs:
#   Window: win
#   float: total_current_dose
#   Point: origin
#   int: hour
# Outputs:
#   NONE
def displayHourlyInfo(win, total_current_dose, origin, hour):
    # Create points for the rectangle
    pt1_x = origin.getX() + hour * 3.63636362 - 0.5
    pt1_y = origin.getY() - 1
    pt2_x = pt1_x + 1
    pt2_y = origin.getY() + total_current_dose * 0.55
    pt1 = Point(pt1_x, pt1_y)
    pt2 = Point(pt2_x, pt2_y)

    # Create the rectangle bar
    rect = Rectangle(pt1, pt2)
    rect.setFill('black')

    # Draw the rectangle
    rect.draw(win)

# Define displaySimulationInfo()
# Inputs:
#   Window: win
#   int: dose_mg
#   float: final_dose
#   int: effective_hr
#   int: overdose_hr
#   int: lethal_hr
# Outputs:
#   NONE
def displaySimulationInfo(win, dose_mg, final_dose, effective_hr, overdose_hr, lethal_hr):
    # Creates the string for the information box
    if effective_hr == None:
        info = str(dose_mg) + ': Ineffective (never enough drug in the body)'
    elif overdose_hr == None:
        info = str(dose_mg) + ': Effective beginning at hour ' + str(effective_hr * 8)
    elif lethal_hr == None:
        info = str(dose_mg) + ': Effective but discomfort beginning at hour ' + str(overdose_hr * 8)
    else:
        info = str(dose_mg) + ': LETHAL'

    # Creates the information box
    txt_x = 30
    txt_y = 75 - (dose_mg * 3) - 4
    txt_pt = Point(txt_x, txt_y)
    if effective_hr == None:
        createText(txt_pt, info, 'black').draw(win)
    elif overdose_hr == None:
        createText(txt_pt, info, 'green').draw(win)
    elif lethal_hr == None:
        createText(txt_pt, info, 'blue').draw(win)
    else:
        createText(txt_pt, info, 'red').draw(win)

    # Creates a rectangle to hide the previous results
    rect = Rectangle(Point(0, 0), Point(130, 24))
    rect.setFill('lightgray')
    rect.setOutline('lightgray')
    rect.draw(win)

    # Determines the string for the results text box
    if effective_hr == None:
        results = 'With a dose of ' + str(dose_mg) + 'mg every 8 hours, the drug was ineffective.'
    elif overdose_hr == None:
        results = 'With a dose of ' + str(dose_mg) + 'mg every 8 hours, the drug became effective at hour ' + str(effective_hr * 8) + '.'
    elif lethal_hr == None:
        results = 'With a dose of ' + str(dose_mg) + 'mg every 8 hours, discomfort began at hour ' + str(overdose_hr * 8) + '.'
    else:
        results = 'With a dose of ' + str(dose_mg) + 'mg every 8 hours, the drug was LETHAL at hour ' + str(lethal_hr * 8) + '.'

    # Creates another text box for the results
    createText(Point(65, 12), results, 'black').draw(win)

# Define checkForButtonClick()
# Inputs:
#   Window: win
#   Rectangle: btn
# Outputs:
#   bool: clicked
def checkForButtonClick(win, btn):
    # Waits for a click from the user
    click = win.getMouse()

    # Gets the points cooresponding to the click
    click_x = click.getX()
    click_y = click.getY()

    # Gets the points cooresponding to the rectangle
    p1 = btn.getP1()
    p2 = btn.getP2()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()

    # Checks for a click within the rectangle
    if (click_x >= p1_x and click_x <= p2_x) and \
       (click_y >= p1_y and click_y <= p2_y):
        clicked = True
    else:
        clicked = False

    return clicked

# Define main()
def main():
    # Prompt user for applicable information
    lethaldose = float(input('How many mg of the drug is lethal? '))
    overdose = float(input('How many mg of the drug is considered an overdose? '))
    effectivedose = float(input('How many mg of the drug is considered effective? '))
    decayrate = float(input('What percentage of the drug should decay every eight hours? '))

    # Validations
    # Call validateDoseInputs()
    lethaldose, overdose, effectivedose = validateDoseInputs(lethaldose, overdose, effectivedose)
    decayrate = validateDecayRate(decayrate)

    # Call simulateDosage()
    win = runSimulation(lethaldose, overdose, effectivedose, decayrate)

    # Gracefully close the simulation with a button click
    # Update the button
    btn = createButton(win, Point(150, 10), Point(170, 15), 'Close the Simulation', 'gray', 'black')

    # Call waitForClick()
    waitForClick(win, btn)

# Call main()
main()
