class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, val):
    if (val <= self.data):
      if self.left:
        self.left.insert(val)
      else:
        self.left = Node(val)
    else:
      if self.right:
        self.right.insert(val)
      else:
        self.right = Node(val)
  
  def contain(self, val):
    if (val == self.data):
      return self.data
    elif (val < self.data and self.left != None):
      return self.left.contain(val)
    elif (val < self.data):
      return None
    elif (val > self.data and self.right != None):
      return self.right.contain(val)
    elif (val > self.data):
      return None
  
  def validate(self, Max=None, Min=None):

    if Max != None and self.data > Max:
      return False
    if Min != None and self.data < Min:
      return False
    if self.left and not(self.left.validate(Max=self.data, Min=Min)):
      return False
    if self.right and not(self.right.validate(Max=Max, Min=self.data)):
      return False
    
    return True
      
      
        
  
def printBST(node):
  buffer = [node]
  while buffer:
    n = buffer.pop(0)
    print(n.data, end=' ')
    if n.left:
      buffer.append(n.left)
      print('left=', n.left.data, end=' ')
    if n.right:
      buffer.append(n.right)
      print('right=', n.right.data, end=' ')
    print()

if __name__ == '__main__':
  n1 = Node(10)
  n1.insert(0)
  n1.insert(12)
  n1.insert(13)
  n1.insert(-12)
  n1.insert(43)
  n1.insert(11)
  n1.insert(4)
  printBST(n1)
  check = n1.contain(43)
  print('it exists = ',check)
  print(n1.validate())
  n1.left.left.right = Node(14)
  print(n1.validate())