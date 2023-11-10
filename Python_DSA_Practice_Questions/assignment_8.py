# -----------------------Stack Using extending list------------------------
# Que:1->
class Stack(list):
    # Que:2
    def is_empty(self):
        return len(self) == 0

    # Que:3
    def push(self, data):
        self.append(data)

    # Que:4
    def pop(self):
        if not self.is_empty():
            # call the parent list class pop() method.(using super() )
            return super().pop()
        else:
            raise AttributeError("Stack Object has no elements.")

    # Que:5
    def peek(self):
        if not self.is_empty():
            return self[-1]
        raise IndexError("Stack object has no elements to peek.")

    # Que:6
    def size(self):
        return len(self)

    # Que:7
    def insert(self):
        raise AttributeError("Can't insert item in Stack Object.")

    # Que:8
    def __iter__(self):
        raise TypeError("Stack Object is not iterable.")


# --------------------------- Testing code ---------------------------
myStack = Stack()
print(myStack.is_empty())
myStack.push(20)
myStack.push(50)
myStack.push(90)
myStack.push(10)
print("This item has pop", myStack.pop())
print(myStack.is_empty())
print("The length of the stack is", myStack.size())
print('This is last element', myStack.peek())
# myStack.insert(0,22)
print()
# To check that Stack is iterable or not.
# for i in myStack:
#     print(i)

# ----------------------------------Questions----------------------
# Que:1-> Define a class Stack to implement stack data structure by extending list
# class.
# Que:2-> Define a method is_empty() to check if the stack is empty in Stack class.
# Que:3-> In Stack class define push() method to add data on to the stack.
# Que:4-> In Stack class define pop() method to remove top element from the stack.
# Que:5-> In Stack class define peek() method to return top element on the stack.
# Que:6-> In Stack class define size() method to return size of the stack that is
# number of items present in the stack.
# Que:7-> Implement a way to restrict use of insert() method of list class from
# Stack object.
# Que:8-> Implement a way to restrict Stack is __iter__() method of list class from
# Stack object that Stack is not iterable.
