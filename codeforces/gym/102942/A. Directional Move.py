# Python3 program to illustrate inserting
# a Node in a Circular Doubly Linked list
# in begging, end and middle
start = None


# Structure of a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Function to insert at the end
def insertEnd(value):
    global start

    # If the list is empty, create a
    # single node circular and doubly list
    if (start == None):
        new_node = Node(0)
        new_node.data = value
        new_node.next = new_node.prev = new_node
        start = new_node
        return

    # If list is not empty

    # Find last node */
    last = (start).prev

    # Create Node dynamically
    new_node = Node(0)
    new_node.data = value

    # Start is going to be next of new_node
    new_node.next = start

    # Make new node previous of start
    (start).prev = new_node

    # Make last previous of new node
    new_node.prev = last

    # Make new node next of old last
    last.next = new_node


# Function to insert Node at the beginning
# of the List,
def insertBegin(value):
    global start

    # Pointer points to last Node
    last = (start).prev

    new_node = Node(0)
    new_node.data = value  # Inserting the data

    # setting up previous and
    # next of new node
    new_node.next = start
    new_node.prev = last

    # Update next and previous pointers
    # of start and last.
    last.next = (start).prev = new_node

    # Update start pointer
    start = new_node


# Function to insert node with value as value1.
# The new node is inserted after the node with
# with value2
def insertAfter(value1, value2):
    global start
    new_node = Node(0)
    new_node.data = value1  # Inserting the data

    # Find node having value2 and
    # next node of it
    temp = start
    while (temp.data != value2):
        temp = temp.next
    next = temp.next

    # insert new_node between temp and next.
    temp.next = new_node
    new_node.prev = temp
    new_node.next = next
    next.prev = new_node


def display():
    global start
    temp = start

    print("Traversal in forward direction:")
    while (temp.next != start):
        print(temp.data, end=" ")
        temp = temp.next

    print(temp.data)

    print("Traversal in reverse direction:")
    last = start.prev
    temp = last
    while (temp.prev != last):
        print(temp.data, end=" ")
        temp = temp.prev

    print(temp.data)


t = 1 # int(input())
for _ in range(t):
    n = int(input())
    s = input()
    start = None
    insertEnd("E")
    insertEnd("S")
    insertEnd("W")
    insertEnd("N")



# # Driver Code
# if __name__ == '__main__':
#     # Start with the empty list
#     start = None
#
#     # Insert 5. So linked list becomes 5.None
#     insertEnd(5)
#
#     # Insert 4 at the beginning. So linked
#     # list becomes 4.5
#     insertBegin(4)
#
#     # Insert 7 at the end. So linked list
#     # becomes 4.5.7
#     insertEnd(7)
#
#     # Insert 8 at the end. So linked list
#     # becomes 4.5.7.8
#     insertEnd(8)
#
#     # Insert 6, after 5. So linked list
#     # becomes 4.5.6.7.8
#     insertAfter(6, 5)
#
#     print("Created circular doubly linked list is: ")
#     display()