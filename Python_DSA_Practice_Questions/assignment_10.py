# Que:1->
from assignment_3 import *


# Que:2->
class Stack:
    def __init__(self):
        # creating SLL class object.
        self.my_stack = SLL()
        self.count_item = 0

    # Que:3->
    def is_empty(self):
        return self.my_stack.is_empty()

    # Que:4->
    def push(self, data):
        self.count_item += 1
        self.my_stack.insert_at_start(data)

    # Que:5->
    def pop(self):
        if not self.is_empty():
            self.count_item -= 1
            self.my_stack.delete_first()

    # Que:6->
    def peek(self):
        if not self.is_empty():
            return self.my_stack.start.item

    # Que:7->
    def size(self):
        return self.count_item


# Testing code
myStack3 = Stack()
print(myStack3.is_empty())
myStack3.push(20)
myStack3.push(50)
myStack3.push(90)
print(myStack3.is_empty())
print('This is a last item:', myStack3.peek())
print(myStack3.size())
# ------------------Stack Using Linked List------------------
# -------------------Questions--------------------------
# Que:1-> Import module containing Singly linked list code in your python file.
# Que:2-> Define a class Stack to implement Stack data structure.Define __init__()
# method to create Singly linked list(SLL) object.
# Que:3-> Define a method is_empty() to check if the stack is empty in Stack class.
# Que:4-> In Stack class define push() method to add data o to the stack.
# Que:5-> In Stack class define pop() method to remove top element from Stack.
# Que:6-> In Stack class define peek() method to return top element on the stack.
# Que:7-> In Stack class define size() method to return size of the stack that is
# number of items present in the stack.
