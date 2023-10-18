#               ----Singly Linked List Practice Questions----
# Que:1-> Define a class Node to describe a node of a singly linked list.
class Node:
    def __init__(self, data=None, next_element_reference=None):
        self.item = data
        self.next = next_element_reference


# Que:2-> Define a class SLL to implement SLL with __init__() method to
# create and initialize start reference variable.
class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        # Que:-> 3
        return self.start is None

    def insert_at_start(self, data):
        # create a node object and insert the next_element reference (Que:-> 4)
        n = Node(data, self.start)
        # insert the reference of n object at the start.
        self.start = n

    def insert_at_last(self, data):
        # create a new Node object (Que:5)
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            # assign first node reference to the temp variable.
            temp = self.start
            # traverse every node with the help of temp of variable.
            while temp.next is not None:
                temp = temp.next
            # when temp.next is none mean we reach at the end of the node
            # then we will have to assign new node reference to temp.next
            temp.next = n
# Que:3-> Define a method is_empty() to check if the linked list is empty in SLL class.
# Que:4-> In class SLL define a method insert_at_start() to insert an element at the starting of the list.
# Que:5-> In class SLL define a method insert_at_last() to insert an
# element at  the end of the list.
