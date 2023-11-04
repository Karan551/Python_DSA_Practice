# -------------------------Stack Using Singly List Class------------------------
# Que:1->
class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    # Que:2
    def is_empty(self):
        return self.start is None

    # Que:3
    def push(self, data):
        node_object = Node(data, self.start)
        self.start = node_object
        self.item_count += 1

    # Que:4
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack has no elements.")

    # Que:5
    def peek(self):
        if not self.is_empty():
            return self.start.item
        raise IndexError("Stack is empty.")

    # Que:6
    def size(self):
        return self.item_count


# Testing code
myStack = Stack()
print("Stack is empty :", myStack.is_empty())
myStack.push(20)
# myStack.push(40)
# myStack.push(60)
print("This is the last item of the stack is :", myStack.peek())
print("The total element in stack is :", myStack.size())
# print("Stack is empty :", myStack.is_empty())
myStack.pop()
# print("This is the last item of the stack is :", myStack.peek())
print()
print("The total element in stack is :", myStack.size())

# ------------------------Questions------------------------------------
# Que:1-> Define a class Stack to implement Stack Data Structure using singly linked
# list concept. Define __init__() method to initialize start reference variable and
# item_count variable to keep track of number of elements in the Stack.
# Que:2-> Define a method is_empty() to check if the stack is empty in Stack class.
# Que:3-> In Stack class define push() method to add data on to stack.
# Que:4-> In Stack class define pop() method to remove top element from Stack.
# Que:5-> In Stack class define peek() method to return top element on the stack.
# Que:6-> In Stack class define size() method to return size of the stack that is
# number of items present in the Stack.
