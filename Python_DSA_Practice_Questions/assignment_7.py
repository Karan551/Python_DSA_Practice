# -----------------------------Stack Using List------------------------------
# Que:1
class Stack:
    def __init__(self):
        self.lst = []

    # Que:2
    def is_empty(self):
        return len(self.lst) == 0

    # Que:3
    def push(self, data):
        self.lst.append(data)

    # Que:4
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            raise IndexError("Stack is empty.")

    # Que:5
    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Stack is empty.")

    # Que:6
    def size(self):
        return len(self.lst)


#    Testing code
st = Stack()
print('Stack is empty:', st.is_empty())
st.push(20)
st.push(30)
st.push(40)
# st.pop()
# print('Removed element is :', st.pop())
# st.push(50)
# print("The top element of the stack is :", st.peek())
print('Stack is empty:', st.is_empty())
print("The size of the Stack is:", st.size())

#       ------------------------Questions---------------------------
# Que:1-> Define a class Stack to implement Stack Data Structure using list. Define
# __init__() method to create an empty as instance object member of stack.
# Que:2-> Define a method is_empty() to check if the stck is empty in Stack class.
# Que:3-> In Stack class define push() method to add data on to the stack.
# Que:4-> In Stack class define pop() method to remove top element (last element) from
# the stack.
# Que:5-> In Stack class define peek() method to top element on the stack.
# Que:6-> In Stack class define size() method to return size of the stack that is
# number of items present in the stack.
