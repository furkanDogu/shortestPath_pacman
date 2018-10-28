import turtle
class Pen(turtle.Turtle):
    def __init__(self, color):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(color)
        self.penup()
        if (color !="yellow"):
            self.speed(100)
        else:
            self.speed(10)
