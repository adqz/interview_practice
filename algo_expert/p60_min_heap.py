class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)

        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = (currentIdx * 2) + 1

        while childOneIdx <= endIdx:
            # Checking if we have second child
            if (currentIdx * 2) + 2 <= endIdx:
                childTwoIdx = (currentIdx * 2) + 2
            else:
                childTwoIdx = None
            # Find which child is smaller in value
            if childTwoIdx is not None and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            # Swap if value at current index is less than value at child
            if heap[currentIdx] < heap[idxToSwap]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx * 2) + 1
            else:
                break

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]: #change to > for MaxHeap
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1) // 2
    
    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]
    
    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)

        return valueToRemove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    # O(1) time | O(1) space
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
    