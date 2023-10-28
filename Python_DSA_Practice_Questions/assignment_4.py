# ----------------- Doubly Linked List Questions -------------
# Que:9 (Ok tested).
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

    # Que:4 (Ok Tested.)
    def insert_at_start(self, data):
        node_object = Node(None, data, self.start)
        # if DLL is not empty then
        if not self.is_empty():
            self.start.prev = node_object
            # connect the node with start
            self.start = node_object
        else:
            self.start = node_object
            node_object.next = None

    # Que:-5   ( Ok Tested. )
    def insert_at_last(self, data):
        # Get the reference of first node_object.
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
                # we get last node reference in temp variable after
                # ending the loop.
        # create a node_object.
        node_object = Node(temp, data, None)
        # temp(self.start) None means DLL contains only one element.
        if temp is None:
            self.start = node_object
        else:
            # join the node with second last node_object.
            temp.next = node_object

    # Que:6 (Ok Tested)
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return True
            temp = temp.next
        else:
            return False

    # Que:7 (Ok Tested)
    def insert_after(self, search_data, insert_data):
        if self.is_empty():
            return None
        temp = self.start
        if self.search(search_data):
            while temp is not None:
                if temp.item == search_data:
                    node_object = Node(temp, insert_data, temp.next)
                    temp.next = node_object
                temp = temp.next

    # Que:8 (Ok Tested)
    def printObject(self):
        # Get the reference of first node_object.
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    # Que:9
    def __iter__(self):
        return Iterator(self.start)

    # Que:10 (Ok Tested.)
    def delete_first(self):
        # if list is empty then do nothing.
        if self.is_empty():
            pass
        # if list contains only one node_object.
        if self.start.next is None:
            self.start = None
        # If list contains at least two node objects.
        else:
            self.start = self.start.next
            self.start.prev = None

    # Que:11 (Ok Tested)
    def delete_last(self):
        # Get the reference of first Node.
        if not self.is_empty():
            # If list has only one node_object then assign None in start.
            if self.start.next is None:
                self.start = None
            # If list has at least two node_objects then we will do this.
            else:
                # Get the reference of first variable.
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None

        # If list is empty then do nothing.
        else:
            pass

    # Ye abhi create karna hai.
    def delete_item(self):
        pass


# Que:3-> Define a method is_empty() to check if the linked list
# is empty in DLL class.
# Que:4-> In class DLL define a method insert_at_start() to insert an
# element at the starting of the list.
# Que:5-> In class DLL define a method insert_at_last() to
# insert an element at  the end of the list.
# Que:6-> In class DLL define a method search() to find the node with specified
# element value.
# Que:7-> In class DLL define a method insert_after() to insert a new node after
# a given node list.
# Que:8-> In class DLL define a method to print all elements of the list.
# Que:9-> In class DLL define a method to access all elements of the list in
# a sequence.
# Que:10-> In class DLL define a method  delete_first() to delete first element.
# Que:11-> In class DLL define a method delete_last() to delete last element.
# Que:12-> In class DLL define a method delete_item() to delete specified
# element from the list.


# Testing code
myList = DLL()
# myList.insert_at_start(21)
myList.insert_at_start(51)
# myList.insert_at_start(101)
# myList.insert_at_last(500)
# myList.insert_at_last(400)
# myList.insert_at_last(1000)

myList.printObject()
# a = int(input("\n enter the data that you want to search: "))
# b = int(input(" enter the data that you want to insert: "))
# myList.delete_first()
# myList.delete_first()
# myList.delete_first()
# myList.delete_first()
myList.delete_first()

# myList.insert_after(a, b)
print()
myList.printObject()
# print(myList.search(a))
# for i in myList:
#     print(i)
