class InorderIterator:
    def __init__(self, root):
        self.stack = []
        node = root
        while node:
            self.stack.append(node.data)
            node = node.left
        
    def hasNext(self):
        if not self.stack:
            return False
        else:
            return True

    # getNext returns null if there are no more elements in tree
    def getNext(self):
        if not self.stack:
            return None
        
        curr_node = self.stack.pop()
        temp_node = curr_node.right
        while temp_node != None:
            self.stack.append(temp_node)
            temp_node = temp_node.left
        
        return curr_node
        

def inorder_using_iterator(root):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        result += ptr.data + " "
    return result