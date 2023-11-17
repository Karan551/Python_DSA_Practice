class Node:
    def __init__(self, data=None, next_ref=None):
        self.item = data
        self.next = next_ref

# Que:1
class Queue:
    def __init__(self):
        self.start = None
        self.front = None
        self.rear = None
        self.item_count = 0

    # Que:2
    def is_empty(self):
        return self.start is None

    # Que:3
    def enqueue(self, data):
        node_object = Node(data, self.start)
        self.start = node_object
        self.rear = node_object
        self.item_count += 1

    # Que:4
    def dequeue(self):
        if not self.is_empty():
            temp = self.start
            # IF queue contains only one item then do this.
            if self.start.next is None:
                # self.front = self.start.item
                self.start = None
                # decrease the item count variable value.
                self.item_count -= 1
            else:
                while temp.next.next is not None:
                    temp = temp.next
                # self.front = temp.item
                temp.next = None
                self.item_count -= 1
        else:
            raise IndexError("Queue is underflow.")

    # Que:5
    def get_rear(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Queue is Empty.")

    # Que:6
    def get_front(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        raise IndexError("Queue is empty.")

    # Que:7
    def size(self):
        return self.item_count


# ---------------Testing code-------------------
myQueue = Queue()
print(myQueue.is_empty())
myQueue.enqueue(50)
myQueue.enqueue(20)
# myQueue.enqueue(40)
# myQueue.enqueue(80)
# myQueue.enqueue(10)
# myQueue.dequeue()
myQueue.dequeue()
print("This is the rear (latest) element: ", myQueue.get_rear())
print("This is the front (oldest) element: ", myQueue.get_front())
print(myQueue.is_empty())
print("The size of the queue is :", myQueue.size())
# print("This the oldest element of queue is :", myQueue.get_front())
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
