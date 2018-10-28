import turtle
import Pen
class Map(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        screen = turtle.Screen()
        self.screen.setup(700, 700)
        self.screen.bgcolor("black")

    def drawArea(self, mapc):
        map = mapc.copy()
        penWhite = Pen.Pen("white")
        for y in range(len(map)):
            for x in range(len(map[y])):

                character = map[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)
                if(character == 1):
                    penWhite.goto(screen_x,screen_y)
                    penWhite.stamp()
                elif(character ==9):
                    penRed = Pen.Pen("red")
                    penRed.goto(screen_x, screen_y)
                    penRed.stamp()
                elif(character == 5):
                    penYellow = Pen.Pen("yellow")
                    penYellow.goto(screen_x,screen_y)
                    penYellow.stamp()



    def cleanArea(self):
        self.screen.reset()
        self.screen.bgcolor("black")

    def printPath(self, path):
        newPath = path.copy()
        newPath.reverse()
        pen = Pen.Pen("yellow")
        for y in range(len(newPath)):
            for x in range(len(newPath[y])):
                if (x == 0):
                    screen_x = -288 + (newPath[y][x]* 24)
                else:
                    screen_y = 288 - (newPath[y][x] * 24)

            pen.goto(screen_x, screen_y)
            pen.stamp()
    def printPathBFS(self, path):
        newPath = path.copy()
        pen = Pen.Pen("yellow")
        for y in range(len(newPath)):
            for x in range(len(newPath[y])):
                if (x == 1):
                    screen_x = -288 + (newPath[y][x]* 24)
                else:
                    screen_y = 288 - (newPath[y][x] * 24)

            pen.goto(screen_x, screen_y)
            pen.stamp()
