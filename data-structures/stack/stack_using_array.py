class Stack:
    def __init__(self):
        self.data = []
    def length(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self,element):
        self.data.append(element)
    def pop(self):
        if self.is_empty():
            pass
        else:
            return self.data.pop()
    def top(self):
        if self.is_empty():
            pass
        else:
            return self.data[-1]