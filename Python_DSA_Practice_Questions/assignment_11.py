# Que:1
from assignment_3 import *


# Que:2
class Stack(SLL):
    def __init__(self):
        # call the parent class __init__ using super() method.
        super().__init__()
        # We can do this like this.(Alternative of first method.)
        # SLL.__init__(self)
        # creating a variable to know the size of the Stack.
        self.item_count = 0

    # Que:3->
    def is_empty(self):
        return super().is_empty()

    # Que:4->
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1

    # Que:5->
    def pop(self):
        if not self.is_empty():
            self.item_count -= 1
            self.delete_first()
        else:
            raise IndexError("Not remove element from stack.")

    # Que:6->
    def peek(self):
        if not self.is_empty():
            return self.start.item
        raise IndexError("Can't get item from stack object.")

    # Que:7->
    def size(self):
        return self.item_count

    def __iter__(self):
        raise TypeError("Stack is not iterable.")


# ------------------------Testing code-----------------------
myStack = Stack()
print(myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(90)
myStack.push(70)
myStack.push(30)
# myStack.push(80)
myStack.pop()
print(myStack.is_empty())
print('This is last item of stack:', myStack.peek())
print("The total element in the stack is :", myStack.size())

# -----------Stack Implementation by extending Singly Linked List-----------
# -------------------------------Questions------------------------------
# Que:1->Import module Singly linked list code in your python file.
# Que:2-> Define a class Stack to implement Stack data structure by inheriting SLL
# class.
# Que:3-> Define a method is_empty() to check if the stack is empty in Stack class.
# Que:4-> In Stack class define push() method to add data on to Stack.
# Que:5-> In Stack class define pop() method to remove top element from Stack.
# Que:6-> In Stack class define peek() method to return top element on Stack.
# Que:7-> In Stack class define size() method to return the size of the Stack that
# is number of items in the Stack.
