from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300, 280)
        self.color("Green")
        self.pensize(7)
        self.pendown()
        self.seth(0)
        self.forward(1000)