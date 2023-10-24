class SLLIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        # store the value in item
        item = self.current.item
        # change the reference variable.
        self.current = self.current.next
        return item


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

    # Que:-> 3
    def is_empty(self):
        return self.start is None

    # (Que:-> 4)
    def insert_at_start(self, data):
        # create a node object and insert the next_element reference
        node_object = Node(data, self.start)
        # insert the reference of n object at the start.
        self.start = node_object

    # (Que:5)
    def insert_at_last(self, data):
        # create a node object.
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

    # ( Que:6 )
    def search(self, data):
        temp = self.start
        # if SLL is not empty then do this operation
        if not self.is_empty():
            # traverse every element in the list.
            while temp is not None:
                if temp.item == data:
                    return f'{temp.item} is in the list.'
                temp = temp.next
            else:
                return False
        else:
            return False

    # Que:-> 7
    def insert_after(self, search_data, insert_data):
        if not self.search(search_data):
            return 'This item is not in the SLL.'
        temp = self.start
        while temp is not None:
            if temp.item == search_data:
                n = Node(insert_data, temp.next)
                temp.next = n
            temp = temp.next

    # Que:8->
    def printObject(self):
        if self.is_empty():
            return 'List is empty Nothing to print.'
        # store the first object reference.
        temp = self.start
        # traverse every object at the end.
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    # create an object of SLLIterator (Que:-9)
    def __iter__(self):
        return SLLIterator(self.start)

    # Que:10
    def delete_first(self):
        # check that list is not empty
        if not self.is_empty():
            # assign second element reference to the start.
            self.start = self.start.next

    # Que:11
    def delete_last(self):
        # if list is not empty then we will delete item.
        if not self.is_empty():
            # if list contains only one item then we will assign
            # None in self.start
            if self.start.next is None:
                self.start = None
            else:
                # get first element reference.
                temp = self.start
                # we start looping to the second element and
                # traverse every element
                while temp.next.next is not None:
                    temp = temp.next
                # assign second last element None
                temp.next = None
        # if list is empty then we will do nothing.
        else:
            pass


# Testing code
myList = SLL()
# result = myList.is_empty()
myList.insert_at_start(20)
# myList.insert_at_start(40)
# myList.insert_at_start(80)
myList.insert_at_last(100)
# myList.insert_at_start(15)
myList.insert_at_last(78)

# myList.insert_after(15, 500)
myList.printObject()
# myList.delete_first()
myList.delete_last()
print('\nafter delete element.')
myList.printObject()
# print()
# print()
# for i in myList:
#     print(i)
# print(result)
# print(myList.search(101))

# Que:3-> Define a method is_empty() to check if the linked list is empty in SLL class.
# Que:4-> In class SLL define a method insert_at_start() to insert an element at the starting of the list.
# Que:5-> In class SLL define a method insert_at_last() to insert an
# element at  the end of the list.
# Que:6-> In a class SLL define a method to search() to find the node
# with specified element value.
# Que:7-> In a class SLL define a method insert_after() to insert
# a new node after a given node of the list.
# Que:8-> In class SLL define a method to print all elements of the
# list.
# Que:9-> In class SLL implement iterator for SLL to access  all
# the elements of the list in a sequence.
# Que:10-> In class SLL define a method delete first() method to
# delete first element from the list.
# Que:11-> In class SLL define a method delete_last() method to
# delete last element from the list.
# Que:12-> In class SLL define a method delete_item() to delete
# specified element from the list.

# abhi last ke three question solve karna hai.