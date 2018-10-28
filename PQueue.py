import Queue
class PQueue(Queue.Queue):
    def __init__(self, map):
        Queue.Queue.__init__(self, map)
    def pop(self):
        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].cost < self.queue[min].cost:
                min = i
        return self.queue.pop(min)

