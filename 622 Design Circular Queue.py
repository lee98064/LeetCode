class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.now_len = 0
        self.rear = -1
        self.font = -1
        print(self.data)

    def enQueue(self, value: int) -> bool:
        if(self.now_len < len(self.data) and self.rear != self.now_len):
            self.data.pop()
            self.data.insert(self.rear + 1,value)
            self.now_len += 1
            self.rear += 1
            self.font = 0
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if(self.now_len > 0 and self.font == 0):
            self.data.pop(0)
            self.data.append(0)
            self.now_len -= 1
            self.rear -= 1
            if(self.rear == -1):
                self.font = -1
            return True
        else:
            return False

    def Front(self) -> int:
        if(self.font == 0):
            return self.data[0]
        else:
            return -1

    def Rear(self) -> int:
        if (self.rear > -1):
            return self.data[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        if (self.rear != -1 and self.font != -1):
            return False
        else:
            return True

    def isFull(self) -> bool:
        if(self.now_len == len(self.data)):
            return True
        else:
            return False
