class Iterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Que:1->
class Node:
    def __init__(self, data=None, next_ref=None):
        self.item = data
        self.next = next_ref


# Que:2
class CLL:
    def __init__(self, last=None):
        self.last = last

    # Que:3
    def is_empty(self):
        return self.last is None

    # Que:4(This is okay tested.)
    def insert_at_start(self, data):
        node_object = Node(data)
        if not self.is_empty():
            # we pass first existing node reference into the
            # new node_object
            node_object.next = self.last.next
            self.last.next = node_object
        else:
            # if node is empty then we pass reference of self node in
            # itself next.
            node_object.next = node_object
            # And also passed node object reference in last.
            self.last = node_object

    # This is okay tested.
    def insert_at_last(self, data):
        if not self.is_empty():
            node_object = Node(data, self.last.next)
            self.last.next = node_object
            self.last = node_object
        else:
            # due to this create an infinite loop.
            node_object = Node(data)
            node_object.next = node_object
            self.last = node_object

    # This is checked okay.
    def search(self, data):
        if self.is_empty():
            return None
        start = self.last.next
        while start.next != self.last.next:
            if start.item == data:
                return True
            start = start.next
        if start.item == data:
            return True
        else:
            return False

    # this worked okay tested.
    def insert_after(self, search_data, insert_data):
        if self.is_empty():
            return 'This is empty list.'
        if self.search(search_data):
            temp = self.last.next
            node_object = Node(insert_data)
            while temp.next != self.last.next:
                # compare each node item to the search item.
                if temp.item == search_data:
                    node_object.next = temp.next
                    temp.next = node_object
                    return True
                temp = temp.next
            # compare last item to the search data.
            if temp.item == search_data:
                # assign value that in the temp's next into the node_object's next.
                node_object.next = temp.next
                # last item's in next of node_object reference.
                temp.next = node_object
                # assign node_object reference into the last.
                self.last = node_object
                return True
        else:
            return "Please Enter a valid item that into the list."

    # this is ok Checked
    def delete_first(self):
        # getting first variable reference
        first_var_reference = self.last.next
        self.last.next = first_var_reference.next

    def delete_last(self):
        if self.is_empty():
            return None
        temp = self.last.next
        # if list contains only item then we will assign None in last.
        if temp.next == temp:
            self.last = None
        else:
            # We will start loop when list contains minimum two node_objects.
            # Starting looping and To get the second last node reference.
            while temp.next != self.last:
                temp = temp.next
            # assign first last node reference into second last node reference.
            temp.next = self.last.next
            # And assign second last node reference into the last.
            self.last = temp

    # this is ok tested.
    def printObject(self):
        if self.is_empty():
            return None
        if not self.is_empty():
            # this is first node reference
            temp = self.last.next
            while temp.next != self.last.next:
                print(temp.item, end=' ')
                temp = temp.next
            # print the last value.
            print(temp.item)

    def __iter__(self):
        pass
        # return Iterator(self.last.next)


# Testing Code.
myList = CLL()
myList.insert_at_start(555)
myList.insert_at_start(50)
# myList.insert_at_start(10)
# myList.insert_at_last(2023)
# this worked .
# myList.delete_first()
# myList.delete_first()
# myList.insert_at_last(8)
myList.printObject()
print(myList.delete_last())
print(myList.delete_last())

myList.printObject()
# x = int(input('Enter the data that you want to search'))
# y = int(input("Enter the data that you want to insert: "))
# a = myList.search(x)
# print(a)
print()
# a = myList.insert_after(x, y)
# myList.printObject()
# print('result', a)
# print(myList.is_empty())

# myList.printObject()
print()
print()
# for i in myList:
#     print(i)
