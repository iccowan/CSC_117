# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab26 OOPS 2
# 17 Apr 2019
# CUSTOMER CLASS

# Customer
# Attributes:
#   String lastName
#   String firstName
#   String email
#   float moneySpent
# Methods:
#   String getLastName()
#   String getFirstName()
#   String getFullName()
#   String getEmail()
#   float getMoneySpent()
#   void setLastName(String)
#   void setFirstName(String)
#   void setEmail(String)
#   void setMoneySpent(float)
class Customer:
    def __init__(self, last, first, email, money):
        self.__lastName = last
        self.__firstName = first
        self.__email = email
        self.__moneySpent = money

    def __str__(self):
        return self.__firstName + " " + self.__lastName + " (" + self.__email + ")"

    def getLastName(self):
        return self.__lastName

    def getFirstName(self):
        return self.__firstName

    def getFullName(self):
        return self.getFirstName() + self.getLastName()

    def getEmail(self):
        return self.__email

    def getMoneySpent(self):
        return self.__moneySpent

    def getMoneySpentStr(self):
        return "$" + str("{:.2f}".format(self.__moneySpent))

    def setLastName(self, last):
        self.__lastName = last

    def setFirstName(self, first):
        self.__firstName = first

    def setEmail(self, email):
        self.__email = email

    def setMoneySpent(self, money):
        self.__moneySpent = money
