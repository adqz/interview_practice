# @author: adnan
class Stack():
  '''
  This class implements the classic stack data structure using python lists.
  Stacks operate on a LIFO basis (Last In First Out)
  '''
  def __init__(self, maxLimit = 3):
    self.stackArray = []
    self.maxLimit = maxLimit
    self.top = 0

  def __str__(self):
    return str(self.stackArray)

  def push(self, data):
    if self.top >= self.maxLimit:
      return ('Max limit reached. Cannot add data to stack')
    self.stackArray.append(data)
    self.top += 1

  def pop(self):
    if self.top == 0:
      return ('Nothing to pop')
    self.top -= 1
    return self.stackArray.pop()

  def size(self):
    return len(self.stackArray)

  def peek(self):
    return self.stackArray[self.size() - 1]

if __name__ == '__main__':
  s = Stack()
  s.push(4)
  s.push(7)
  s.push(9)
  print(s)
  # print(s.pop())
  # print(s.pop())
  # print(s.pop())
  # print(s.pop())
  # print(s)