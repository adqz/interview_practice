# @author: adnan
class Stack():
  '''
  This class implements the classic stack data structure using python lists.
  Stacks operate on a LIFO basis (Last In First Out)
  '''
  def __init__(self, maxLimit = 100):
    self.stackArray = []
    self.maxLimit = maxLimit
    self.top = 0

  def __str__(self):
    return str(self.stackArray)

  def push(self, data):
    if self.top >= self.maxLimit:
      raise IndexError('Max limit reached')
    self.stackArray.append(data)
    self.top += 1

  def pop(self):
    if self.top == 0:
      raise IndexError('No elements to pop')
    self.top -= 1
    return self.stackArray.pop()

  def size(self):
    return len(self.stackArray)

  def peek(self):
    if self.size() != 0:
      return self.stackArray[self.size() - 1]
    return None
  def isEmpty(self):
    return self.size() == 0

def reverseStackRecursive(stack1):
  '''
  Checks whether a given string is a palindrome or not using stacks.
  Can also be done using lists
  '''
  assert isinstance(stack1, Stack)
  reversedStack = Stack(maxLimit=stack1.size())
  while not(stack1.isEmpty()):
    reversedStack.push(stack1.pop())
  return reversedStack


def createStackFromString(s):
  assert isinstance(s, str)
  stack = Stack(maxLimit=len(s))
  for char in s:
    stack.push(char)
  return stack

if __name__ == '__main__':
  s1 = createStackFromString('abcd')
  print(reverseStackRecursive(s1))