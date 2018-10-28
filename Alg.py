import numpy as np
import Node
import Queue

class Alg():
    def __init__(self):
        self.isVisitedArr = list(np.zeros((24, 24)))
        self.isFound = False
        self.path = None

    def organizeVisitedArr(self):
        # setting isVisitedArr according to values in given game map
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.isVisitedArr[x][y] = (0,1)[self.map[x][y] == 1]

    def simplifyCheck(self, x, y):
        return self.isVisitedArr[x][y] != 1 and self.map[x][y] != 5 and self.map[x][y] != 2

    def visit(self, node):
        if self.map[node.x][node.y] == 9:
            self.foundTarget(node)
        else:
            self.map[node.x][node.y] = 2
            self.isVisitedArr[node.x][node.y] = 1
    def run(self, map, queue):
        self.map = map
        self.queue = queue
        self.organizeVisitedArr()
        positions = {
            "x": 1,
            "y": 2
        }
        startingNode = Node.Node(positions, "starting")
        self.queue.push(startingNode)
        self.loopAllMap()
        return self.convertPathToArr()


    def findChildren(self, node):
        horizontal = [1, -1, 0, 0]
        vertical = [0, 0, 1, -1]
        children = []

        children.append(self.simplifyCheck(node.x + horizontal[0], node.y + vertical[0]))
        children.append(self.simplifyCheck(node.x + horizontal[1], node.y + vertical[1]))
        children.append(self.simplifyCheck(node.x + horizontal[2], node.y + vertical[2]))
        children.append(self.simplifyCheck(node.x + horizontal[3], node.y + vertical[3]))
        self.addChildren(node, children)

    def addChildren(self, node, children):
        horizontal = [1, -1, 0, 0]
        vertical = [0, 0, 1, -1]

        for i in range(len(children)):
            if children[i] == True:
                positions = {
                    "x": node.x + horizontal[i],
                    "y": node.y + vertical[i],
                }
                childNode = Node.Node(positions, node)
                self.queue.push(childNode)

    def loopAllMap(self):
        if (self.isFound == False):
            poppedNode = self.queue.pop()
            self.visit(poppedNode)
            self.findChildren(poppedNode)
            self.loopAllMap()

    def foundTarget(self, node):
        self.isFound = True
        path = []
        path.insert(0,node)
        while(node.parent != "starting"):
            path.insert(0, node.parent)
            node = node.parent
        self.path = path

    def convertPathToArr(self):
        newPath = []
        for node in self.path:
            newPath.append([node.x, node.y])
        return newPath

