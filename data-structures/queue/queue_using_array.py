class Queue:
    def __init__(self):
        self.data = []
        self.start = 0
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0

    def enqueue(self,element):
        self.data.append(element)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            pass
        else:
            deq_ele = self.data[self.start]
            self.data[self.start] = None
            self.start += 1
            self.size -= 1
            return deq_ele

    def first(self):
        if self.is_empty():
            pass
        else:
            return self.data[self.start]