# Ian Cowan
# Mar 04 2019
# Problem 6 on page 230
# Calories from Fat and Carbs

# Define calFat()
# Inputs:
#   float: fat
# Outputs:
#   float: cal_fat
def calFat(fat):
    # Calculation
    cal_fat = fat * 9

    # Returns the calories from fat
    return cal_fat

# Define calCarb()
# Inputs:
#   float: carb
# Outputs:
#   float: cal_carb
def calCarb(carb):
    # Calculation
    cal_carb = carb * 4

    # Returns the calories from carbs
    return cal_carb

# Define main()
def main():
    # Prompt the user from calories from fat and from carbs
    cal_fat = float(input('Grams of Fat: '))
    cal_carb = float(input('Grams of Carbs: '))

    # Calculates the total calories
    cal = calFat(cal_fat) + calCarb(cal_carb)

    # Returns the total calories
    print('The total calories are:', cal)

# Call main()
main()
