class Linkedlist:
    class Node:
        __slots__ = 'element', 'next_node'

        def __init__(self, element, next_node):
            self.element = element
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0