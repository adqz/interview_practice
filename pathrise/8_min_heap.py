'''
eg - [75,x,x,x,x,x]

 0 1 2 3  4  5
[1 3 8 20 32 75]
 0 1 1 2  2  2

heap = [75,20,3,8,32,1]
'''
import heapq

class MinHeap:
    '''
    TODO:
    __init__
    1. Find min element
    2. Construct binary tree with min element as head - in array form
    3. 
    '''
    
    def __init__(self, heap):
        self.heap = heap
        heapq.heapify(self.heap) 
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def insert(self, val):
        heapq.heappush(self.heap, val)
    
    def remove(self):
        return heapq.heappop(self.heap)
    
    def __repr__(self):
        return str(self.heap)

if __name__ == '__main__':
    l1 = [75,20,3,8,32,1]
    heap = MinHeap(l1)
    print(heap)
    print(heap.peek())
    heap.insert(17)
    heap.insert(44)
    heap.insert(0)
    print(heap)
    print(heap.remove())
    print(heap)