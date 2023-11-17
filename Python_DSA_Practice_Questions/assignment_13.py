class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


# Que:1
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    # Que:2
    def is_empty(self):
        return self.front is None

    # Que:3
    def enqueue(self, data):
        node_object = Node(data)
        # if Queue is empty then do this operation
        if self.is_empty():
            self.front = node_object
        # if Queue is not empty then do this operation
        else:
            # assign new node_object reference to the last Node object in next
            self.rear.next = node_object
        self.rear = node_object
        self.item_count += 1

    # Que:4
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    # Que:5
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        else:
            return self.rear.item

    # Que:6
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        else:
            return self.front.item

    # Que:7
    def size(self):
        return self.item_count


# ------------------------------Testing code--------------------------
# creating an object of Queue class
myQueue = Queue()
print("Queue is empty or not:", myQueue.is_empty())
myQueue.enqueue(20)
myQueue.enqueue(40)
# myQueue.enqueue(50)
# myQueue.enqueue(60)
print("The latest element (rear) of the Queue is:", myQueue.get_rear())
print("The oldest element (front) of the Queue is:", myQueue.get_front())
print("The size of the Queue is :", myQueue.size())
print("Queue is empty or not:", myQueue.is_empty())
myQueue.dequeue()
print()
print("The latest element (rear) of the Queue is:", myQueue.get_rear())
print("The oldest element (front) of the Queue is:", myQueue.get_front())
print("The size of the Queue is :", myQueue.size())

# ------------------------------Questions--------------------------
# --------------Queue using Singly linked List concept-----------
# Que:1-> Define a class Queue to implement queue data structure using
# singly linked list concept. Define __init__() method to initialize
# front and rear reference variable and item_count variable to keep track
# of number of elements in the Queue.
# Que:2-> Define a method is_empty() to check if teh queue is empty in Queue class.
# Que:3-> In Queue class define a method enqueue() method to add data into the queue.
# Que:4-> In Queue class define dequeue() method to remove front element of the queue.
# Que:5-> In Queue class define get_front() method to return front element of the queue.
# Que:6-> In Queue class define get_rear() method to return rear element of the queue.
# Que:7-> In Queue class define size() method to return size of the queue
# that is number of items present in the queue.
