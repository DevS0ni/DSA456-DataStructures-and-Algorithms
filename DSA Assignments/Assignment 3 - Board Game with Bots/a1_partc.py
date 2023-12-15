#    Main Author: Sarah Haque: 
#    Main Reviewer: Dev Alpeshbhai Soni:

# The provided classes implement the Stack, Queue, and Deque data structures.
# All the classes make use of the Python list to maintain the data elements.


class Stack:
    def __init__(self, cap=10):
        # Initializes the Stack with a given capacity or a default of 10 if not provided.
        # The _stack will store our elements, and _size will keep track of the number of elements.
        self._stack = [None] * cap
        self._size = 0
        self._capacity = cap

    def capacity(self):
        # Returns the capacity of the Stack.
        return self._capacity

    def push(self, data):
        # If the stack is full, resize it (double the capacity)
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        # Adds data to the top of the Stack.
        self._stack[self._size] = data
        self._size += 1

    def pop(self):
        # If the stack is empty, raise an error.
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        
        # Removes the newest value from the Stack and returns it.
        self._size -= 1
        data = self._stack[self._size]
        self._stack[self._size] = None  # Optional: free up space
        return data

    def get_top(self):
        # Returns the newest value from the Stack without removing it.
        # Returns None if the Stack is empty.
        if self.is_empty():
            return None
        return self._stack[self._size - 1]

    def is_empty(self):
        # Returns True if the Stack is empty, False otherwise.
        return self._size == 0

    def __len__(self):
        # Returns the number of values in the Stack.
        return self._size

    def _resize(self, new_capacity):
        # Private method to resize the underlying list.
        new_stack = [None] * new_capacity
        for i in range(self._size):
            new_stack[i] = self._stack[i]
        self._stack = new_stack
        self._capacity = new_capacity

class Queue:
    def __init__(self, cap=10):
        # Initializes the Queue with a given capacity or a default of 10 if not provided.
        # The _queue will store our elements, and _front and _size will help manage them.
        self._queue = [None] * cap
        self._front = 0  # Index of the front element
        self._size = 0  # Number of elements currently in the queue
        self._capacity = cap

    def capacity(self):
        # Returns the capacity of the Queue.
        return self._capacity

    def enqueue(self, data):
        # If the queue is full, resize it (double the capacity)
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        # Adds data to the back of the Queue.
        back_index = (self._front + self._size) % self._capacity
        self._queue[back_index] = data
        self._size += 1

    def dequeue(self):
        # If the queue is empty, raise an error.
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        
        # Removes the oldest value from the Queue and returns it.
        data = self._queue[self._front]
        self._queue[self._front] = None  # Optional: free up space
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return data

    def get_front(self):
        # Returns the oldest value from the Queue without removing it.
        # Returns None if the Queue is empty.
        if self.is_empty():
            return None
        return self._queue[self._front]

    def is_empty(self):
        # Returns True if the Queue is empty, False otherwise.
        return self._size == 0

    def __len__(self):
        # Returns the number of values in the Queue.
        return self._size

    def _resize(self, new_capacity):
        # Private method to resize the underlying list.
        new_queue = [None] * new_capacity
        for i in range(self._size):
            new_queue[i] = self._queue[(self._front + i) % self._capacity]
        self._queue = new_queue
        self._front = 0
        self._capacity = new_capacity




class Deque:
    def __init__(self, cap=10):
        # Initializes the Deque with a given capacity or a default of 10 if not provided.
        # The _deque will store our elements, and _front and _size will help manage them.
        self._deque = [None] * cap
        self._front = 0  # Index of the front element
        self._size = 0  # Number of elements currently in the deque
        self._capacity = cap

    def capacity(self):
        # Returns the capacity of the Deque.
        return self._capacity

    def push_front(self, data):
        # If the deque is full, resize it (double the capacity)
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        # Decrement the front index (and wrap around if necessary)
        self._front = (self._front - 1) % self._capacity
        self._deque[self._front] = data
        self._size += 1

    def push_back(self, data):
        # If the deque is full, resize it (double the capacity)
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        # Adds data to the back of the Deque.
        back_index = (self._front + self._size) % self._capacity
        self._deque[back_index] = data
        self._size += 1

    def pop_front(self):
        # If the deque is empty, raise an error.
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        
        # Removes the front value from the Deque and returns it.
        data = self._deque[self._front]
        self._deque[self._front] = None  # Optional: free up space
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return data

    def pop_back(self):
        # If the deque is empty, raise an error.
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        
        # Removes the back value from the Deque and returns it.
        back_index = (self._front + self._size - 1) % self._capacity
        data = self._deque[back_index]
        self._deque[back_index] = None  # Optional: free up space
        self._size -= 1
        return data

    def get_front(self):
        # Returns the front value from the Deque without removing it.
        # Returns None if the Deque is empty.
        if self.is_empty():
            return None
        return self._deque[self._front]

    def get_back(self):
        # Returns the back value from the Deque without removing it.
        # Returns None if the Deque is empty.
        if self.is_empty():
            return None
        back_index = (self._front + self._size - 1) % self._capacity
        return self._deque[back_index]

    def is_empty(self):
        # Returns True if the Deque is empty, False otherwise.
        return self._size == 0

    def __len__(self):
        # Returns the number of values in the Deque.
        return self._size

    def __getitem__(self, k):
        # Returns the k'th value from the front of the Deque without removing it.
        if k < 0 or k >= self._size:
            raise IndexError('Index out of range')
        
        return self._deque[(self._front + k) % self._capacity]

    def _resize(self, new_capacity):
        # Private method to resize the underlying list.
        new_deque = [None] * new_capacity
        for i in range(self._size):
            new_deque[i] = self._deque[(self._front + i) % self._capacity]
        self._deque = new_deque
        self._front = 0
        self._capacity = new_capacity
