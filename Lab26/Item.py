# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab26 OOPS 2
# 17 Apr 2019
# ITEM CLASS

# Item
# Attributes:
#   String __name
#   float __price
#   String __itemType
#   int __quantity
# Methods:
#   String getName()
#   float getPrice()
#   String getType()
#   int getQuantity()
#   void setName(String)
#   void setPrice(float)
#   void setType(String)
#   void setQuantity(int)
class Item:
    def __init__(self, name, price, itemType, quantity):
        self.__name = name
        self.__price = price
        self.__itemType = itemType
        self.__quantity = quantity

    def __str__(self):
        return self.__name + " (" + str(self.__quantity) + " x $" + str("{:.2f}".format(self.__price))+ ")"

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getType(self):
        return self.__itemType

    def getQuantity(self):
        return self.__quantity

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setType(self, itemType):
        self.__itemType = itemType

    def setQuantity(self, quantity):
        self.__quantity = quantity
