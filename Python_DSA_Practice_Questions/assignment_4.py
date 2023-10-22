# ----------------- Doubly Linked List Questions -------------
class Iterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        # when item is empty raise error
        if not self.current:
            raise StopIteration
        # store the item value in data
        data = self.current.item
        # target next element
        self.current = self.current.next
        return data


# Que:1-> Define a class Node to describe a node of a
# doubly linked list.
class Node:
    def __init__(self, prev=None, data=None, next_ref=None):
        self.prev = prev
        self.item = data
        self.next = next_ref


# Que:2-> Define a class DLL to implement Doubly Linked List
# with __init__() method to create and initialize start
# reference variable.
class DLL:
    def __init__(self, start=None):
        self.start = start

    # Que:-3
    def is_empty(self):
        return self.start is None

    # Que:4
    def insert_at_start(self, data):
        node_object = Node(None, data, self.start)
        # if DLL is not empty then
        if not self.is_empty():
            self.start.prev = node_object
        # connect the node with start.(If node is empty then do this)
        self.start = node_object

    # Que:-5
    def insert_at_last(self, data):
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
                # we get last node reference in temp variable after
                # ending the loop.
        # temp None means DLL contains only one element.
        node_object = Node(temp, data, None)
        if temp is None:
            self.start = node_object
        else:
            # node_object = Node(temp, data, None)
            temp.next = node_object

    def printObject(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def __iter__(self):
        return Iterator(self.start)


# Que:3-> Define a method is_empty() to check if the linked list
# is empty in DLL class.
# Que:4-> In class DLL define a method insert_at_start() to insert an
# element at the starting of the list.
# Que:5-> In class DLL define a method insert_at_last() to
# insert an element at  the end of the list.


# Testing code
myList = DLL()
# myList.insert_at_start(21)
myList.insert_at_start(51)
# myList.insert_at_start(101)
# myList.insert_at_last(500)
myList.insert_at_last(400)
# myList.insert_at_last(1000)

myList.printObject()
# for i in myList:
#     print(i)
