# Assuming we have Queue class with enqueue(), dequeue(), and size() methods
from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.queue_store = deque()
        self.queue_temp = deque()
        self.length = 0

    def push(self, value):
        self.queue_store.append(value)
        self.length += 1
        print(self.queue_store)

    def pop(self):
        if self.is_empty:
            return -1
        
        while len(self.queue_store) > 1:
            value = self.queue_store.popleft()
            self.queue_temp.append(value)
        
        value_to_pop = self.queue_store.popleft()
        self.length -= 1
        self.queue_store, self.queue_temp = self.queue_temp, self.queue_store

        return value_to_pop

    def is_empty(self):
        if self.length == 0:
            return True
        return False

