from math import pi


# Que:1-> Define a python class Person with instance object variables  name and
# age. Set instance object variables in __init__ ()method.
# Also define show() method to display name and age of a person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return self.name, self.age


# create an object of Person class
# ram = Person("Ram", 21)
# To show the name of the object.
# print(ram.show())


# Que:2-> Define a class circle with instance object variable radius.Provide
# setter and getter for radius.Also define getArea() method and getCircumference() methods.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return pi * self.radius ** 2

    def getCircumference(self):
        return 2 * pi * self.radius


# create an object of Circle class
# c1 = Circle(10)
# getRadius() of c1 object (This is a getter)
# print(c1.getRadius())
# setRadius() of c1 object (This is a setter)
# c1.setRadius(15)
# print(c1.getRadius())
# getArea of c1 object.
# print(c1.getArea())
# getCircumference() of c1 object.
# print(c1.getCircumference())


# Que:3->Define a class Rectangle with length and width as instance object
# variables.Provide setDimensions(), showDimensions() and getArea() method in it.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def showDimensions(self):
        return self.length, self.width

    def setDimensions(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width


# create an object of Rectangle class
# r1 = Rectangle(10, 20)
# show the dimensions of the rectangle
# print(r1.showDimensions())
# set the dimensions of the rectangle
# r1.setDimensions(25, 30)
# print(r1.showDimensions())
# get the area of the rectangle
# print(r1.getArea())


# Que:4-> Define a Book class with instance object variables book_id,title and
# price. Initialise them via __init__() method. Also define method to show book variables.
class Book:
    def __init__(self, book_id, title, price):
        self.bookId = book_id
        self.title = title
        self.price = price

    def showBookInfo(self):
        return self.bookId, self.title, self.price


# create an object of Book class.
# gita = Book(101, "Gita", 500)
# get the information of gita object.
# print(gita.showBookInfo())


# Que:5-> Define a class Team with instance object variable a list of team
# member names.Provide methods to input member names and display member names.
class Team:
    def __init__(self, team_list: list):
        self.teamList = team_list

    def showTeamMember(self):
        for member in self.teamList:
            print(member)
