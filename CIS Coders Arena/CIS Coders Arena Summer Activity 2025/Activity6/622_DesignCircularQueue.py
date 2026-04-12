class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0]*k
        self.front = -1
        self.rear = -1
        self.size = k
        
    def enQueue(self, value) :
        if self.isFull():
            return False
        if not self.isEmpty():
            self.rear = (self.rear + 1)% self.size
        else:
            self.front = 0
            self.rear = 0
        self.queue[self.rear] = value
        return True
    def deQueue(self):
        if self.isEmpty():
            return False
        if self.rear == self.front:
            self.rear = -1
            self.front = -1
        else:
            self.front = (self.front + 1)% self.size
        return True
        

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1 and self.rear == -1
        
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

        


