import pickle
MARKER = float('inf')

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def serialize(node, stream):
    if not node:
        stream.dump(MARKER)
        return
    stream.dump(node.data)
    serialize(node.left, stream)
    serialize(node.right, stream)

def deserialize(stream):
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None
        
        else:
            node = BinaryTreeNode(data)
            node.left = deserialize(stream)
            node.right = deserialize(stream)
            return node

    except pickle.UnpicklingError:
        return None