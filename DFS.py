class DFS():
    def __init__(self):
        self.map = []
        self.path = []
    def check(self, x, y):
        if(self.map[y][x] == 9):
            self.path.append([x, y])
            return True

        if(self.map[y][x] == 0):
            self.map[y][x] = 2
            #sol
            dx = 1
            dy = 0
            if(self.check(x + dx, y + dy)):
                self.path.append([x, y])
                return True

            #sağ
            dx = -1
            dy = 0
            if(self.check(x + dx, y + dy)):
                self.path.append([x, y])
                return True
            #aşağı
            dx = 0
            dy = -1
            if(self.check(x + dx, y + dy)):
                self.path.append([x, y])
                return True

            #yukarı
            dx = 0
            dy = 1
            if(self.check(x + dx, y + dy)):
                self.path.append([x, y])
                return True

        return False

    def run(self, map):
        self.map = map
        self.check(2,1)
        return self.path
