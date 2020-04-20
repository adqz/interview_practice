class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node) #same as dealing with empty linked list
            return
        
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # remove nodeToInsert and set its next and prev pointers
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # update nearby pointers to point to nodeToInsert
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        # updating node's prev pointer
        node.prev = nodeToInsert
    
    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
    
    # O(p) time | O(1) space, p = position
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1: #at head
            self.setHead(nodeToInsert)
            return
        node = self.head
        currPosition = 1
        while node is not None and position != currPosition:
            node = node.next
            currPosition += 1
        
        if node is not None: #not at tail
            self.insertBefore(node, nodeToInsert)
        else: #at tail
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node #temp variable 
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        # Head check
        if node == self.head:
            self.head = self.head.next
        # Tail check
        if node == self.tail:
            self.tail = self.tail.prev
        # General case
        self.removeNodeBindings(node)
    
    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        
        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False

    def removeNodeBindings(self, node):
        # Update binding
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        # Remove binding
        node.prev = None
        node.next = None

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = dict()
        self.doublyLinkedList = DoublyLinkedList()
        self.currSize = 0
    
    # O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        # Update/Create key value pair
        if key in self.cache:
            self.replaceKeyValuePair(key, value)
        else:
            if self.currSize == self.maxSize:
                self.evictLeastRecentKey()
            else:
                self.currSize += 1
            self.cache[key] = Node(key, value)
        
        # Make it most recent        
        self.updateMostRecent(self.cache[key])

    # O(1) time | O(1) space
    def evictLeastRecentKey(self):
        tail = self.doublyLinkedList.tail
        keyToRemove = tail.key
        self.doublyLinkedList.remove(tail)
        del self.cache[keyToRemove]
    
    # O(1) time | O(1) space
    def updateMostRecent(self, node):
        self.doublyLinkedList.setHead(node)
    
    # O(1) time | O(1) space
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        # Update this key to be most recent
        self.updateMostRecent(self.cache[key])

        return self.cache[key].value

    # O(1) time | O(1) space
    def getMostRecentKey(self):
        return self.doublyLinkedList.head.key

    # O(1) time | O(1) space
    def replaceKeyValuePair(self, key, value):
        if key not in self.cache:
            raise Exception('Key not found')
        
        self.cache[key].value = value
