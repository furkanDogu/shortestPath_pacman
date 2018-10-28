import Queue
class AstarQueue(Queue.Queue):
    def __init__(self, map):
        Queue.Queue.__init__(self, map)
    def pop(self):
        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].fcost < self.queue[min].fcost:
                min = i
        return self.queue.pop(min)