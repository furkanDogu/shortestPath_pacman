from copy import deepcopy
class Queue():
    def __init__(self, map):
        self.queue = list()
        self.map = deepcopy(map)
    def push(self, node):
            if(self.map[node.x][node.y] == 0):
                self.queue.append(node)
                self.map[node.x][node.y] = 1
            if(self.map[node.x][node.y] == 9):
                self.queue.append(node)
    def pop(self):
        if (len(self.queue) > 0):
            return self.queue.pop(0)
    def anyLeft(self):
        return len(self.queue) > 0