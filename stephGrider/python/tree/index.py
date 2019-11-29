class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
  
  def __repr__(self):
    children = ' , '.join([str(child.data) for child in self.children])
    return str(self.data) + ' -> ' + children

  def add(self, data):
    self.children.append(Node(data))
  
  def remove(self, data):
    for i, child in enumerate(self.children):
      if child.data == data:
        del self.children[i]
        break
  
class Tree:
  def __init__(self):
    self.root = None

  def traverseBF(self, fn):
    buffer = [self.root]
    while buffer:
      node = buffer.pop(0)
      print(fn(node).data)
      buffer += node.children
  
  def traverseDF(self, fn):
    buffer = [self.root]
    while buffer:
      node = buffer.pop(0)
      print(node.data)
      buffer = node.children + buffer
  
  def widthCounter(self):
    buffer = [self.root, 's']
    counter = [0]
    while len(buffer) != 1:
      node = buffer.pop(0)
      if node != 's':
        counter[-1] += 1
        buffer += node.children
      else:
        counter.append(0)
        buffer.append(node)
    return counter

  


def add_10(node):
  node.data += 10
  return node


if __name__ == '__main__':
  n1 = Node(20)
  n1.add(0)
  n1.add(40)
  n1.add(-15)
  n1.children[0].add(12)
  n1.children[0].add(-2)
  n1.children[0].add(1)
  n1.children[2].add(-2)
  tree = Tree()
  tree.root = n1
  tree.traverseBF(add_10)
  tree.traverseDF(add_10)
  print(tree.widthCounter())
  # print(tree.root)
  # print(n1.children[0])
  # print(n1.children[2])