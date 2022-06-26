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

    def add_first(self, element):
        new_node = self.Node(element, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, element):
        new_node = self.Node(element, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1

    def add_element(self, element, position):
        new_node = self.Node(element, None)
        tpointer = self.head
        i = 1
        while i < position:
            tpointer = tpointer.next_node
            i += 1
        new_node.next_node = tpointer.next_node
        tpointer.next_node = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            pass
        else:
            first = self.head.element
            self.head = self.head.next_node
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return first

    def remove_last(self):
        if self.is_empty():
            pass
        else:
            tpointer = self.head
            i = 0
            while i < len(self) - 2:
                tpointer = tpointer.next_node
                i += 1
            self.tail = tpointer
            tpointer = tpointer.next_node
            last = tpointer.element
            self.tail.next_node = None
            self.size -= 1
            return last

    def remove_element(self, position):
        if self.is_empty():
            pass
        tpointer = self.head
        i = 1
        while (i < position - 1):
            tpointer = tpointer.next_node
            i += 1
        element = tpointer.next_node.element
        tpointer.next_node = tpointer.next_node.next_node
        self.size -= 1
        return element

    def display(self):
        tpointer = self.head
        while tpointer:
            print(tpointer.element, end="-->")
            tpointer = tpointer.next_node
        print()