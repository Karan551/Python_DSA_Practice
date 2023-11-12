# --------------------------Queue using list--------------------------
class Queue:
    def __init__(self):
        self.my_queue = []

    def is_empty(self):
        return len(self.my_queue) == 0

    def enqueue(self, data):
        self.my_queue.append(data)
        # This is the second method to find the last item of list index.
        # self.rear = self.my_queue[len(self.my_queue) - 1]

    def dequeue(self):
        if not self.is_empty():
            self.my_queue.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def get_rear(self):
        """
        This will give us latest value of queue.
        :return:
        """
        if not self.is_empty():
            return self.my_queue[-1]
        raise IndexError("Queue is underflow.")

    def get_front(self):
        """
        This will give us oldest value of queue.
        :return:
        """
        if not my_queue.is_empty():
            return self.my_queue[0]
        raise IndexError("Queue is underflow.")

    def size(self):
        return len(self.my_queue)


# --------------------Testing code-------------------------
my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(86)
my_queue.enqueue(100)
# print(my_queue.get_rear())
# print(my_queue.is_empty())
my_queue.dequeue()
my_queue.dequeue()
# my_queue.dequeue()
print('This is the rear (latest) value of my_queue:', my_queue.get_rear())
print('This is the front (oldest) value of my_queue:', my_queue.get_front())
print('The size of my_queue is:', my_queue.size())

# --------------------------Queue using list--------------------------
# -------------Questions----------------
# Que:1-> Define a class Queue to implement queue data structure using list.
# Define __init__() method to create an empty list object as instance
# object member of Queue.
# Que:2-> Define a method is_empty() to check if the Queue is empty in
# Queue class.
# Que:3-> In Queue class define enqueue() method to add data at the rear
# end of the queue.
# Que:4> In Queue class define dequeue() method to remove front element
# from the queue.
# Que:5-> In Queue class define get_front() method to return front
# element of the queue.
# Que:6-> In Queue class define get_rear() method to return rear(last)
# element of the queue.
# Que:7-> In Queue class define size() method to return size of the queue
# that is number of items present in the queue.
