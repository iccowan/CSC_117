# Ian Cowan
# Apr 15 2019
# Lab Partner: Jake Pfaller
# Problem 2 on page 477
# Car Class

# Create the Car class
# Attributes:
#   int __year_model
#       The car's year model
#   String __mke
#       The make of the car
#   int __speed
#       The car's current speed
# Methods:
#   accelerate()
#       Adds 5 to the car's speed
#   brake()
#       Subtracts 5 from the car's speed
#   getSpeed()
#       Gets the car's current speed
class Car:
    def __init__(self, year, mke):
        self.__year_model = year
        self.__make = mke
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def getSpeed(self):
        return self.__speed


# Define main()
def main():
    # Create a Car
    myCar = Car(2020, "Subaru Crosstrek")

    # Accelerate the car 5 times
    for i in range(5):
        myCar.accelerate()
        print("Car speed after accelerating 5mph:", myCar.getSpeed())

    # Line break
    print()

    # Brake the car 5 times
    for i in range(5):
        myCar.brake()
        print("Car speed after decelerating 5mph:", myCar.getSpeed())

# Call main()
main()
