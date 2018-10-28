class Node():
    def __init__(self, positions, parent):
        self.x = positions["x"]
        self.y = positions["y"]
        self.parent = parent
        self.cost = None
        self.fcost = None
    def setCost(self, positions):
        self.cost = (positions["x"] + positions["y"]) - (positions["sx"] + positions["sy"])
    def setFCost(self, positions, food): # calculating manhatten
        self.setCost(positions)
        self.fcost = (self.cost + food["x"] + food["y"]) - (self.x +self.y)


