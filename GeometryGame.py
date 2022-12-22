"""
This program leverages basic OOP concepts of python to create a game where 2 random coordinates of a rectangle are generated.
Main goal of the game is for user to guess a coordinate (x,y), such that it should fall inside the coordinates of the rectangle.
User can also guess the area of the rectangle formed and if guessed wrong, user is displayed the message of by how much his guess was off by.
"""
import turtle
from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

"""
Update 21st Dec- Adding a GUI for simpler gameplay using turtle
"""
class GUIRectangle(Rectangle):
    def draw(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)

        #turtle.done()

class GUIPoint(Point):
    def draw(self,canvas,size=5,color='red'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)




# Create rectangle object
gRectangle=GUIRectangle(Point(randint(0, 400), randint(0, 400)),
              Point(randint(10, 400), randint(10, 400)))
turtle=turtle.Turtle()

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
              Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GUIPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

gRectangle.draw(turtle)
user_point.draw(turtle)
