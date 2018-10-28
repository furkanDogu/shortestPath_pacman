
import Node
import Alg
import numpy as np
from copy import deepcopy
class UCS(Alg.Alg):
    def __init__(self):
        Alg.Alg.__init__(self)


    def addChildren(self, node, children):
        horizontal = [1, -1, 0, 0]
        vertical = [0, 0, 1, -1]

        for i in range(len(children)):
            if children[i] == True:
                positions = {
                    "x": node.x + horizontal[i],
                    "y": node.y + vertical[i],
                    "sx": 1,
                    "sy": 2
                }
                childNode = Node.Node(positions, node)
                childNode.setCost(positions)
                self.queue.push(childNode)

    def run(self, map, queue):
        self.map = map
        self.queue = queue
        self.organizeVisitedArr()
        positions = {
            "x": 1,
            "y": 2,
            "sx": 1,
            "sy": 2
        }
        startingNode = Node.Node(positions,"starting")
        startingNode.setCost(positions)
        self.queue.push(startingNode)
        self.loopAllMap()
        return self.convertPathToArr()