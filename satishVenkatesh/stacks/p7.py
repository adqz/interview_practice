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

def reverseStack(stack1):
  '''
  Reverses a given stack using loop
  '''
  assert isinstance(stack1, Stack)
  reversedStack = Stack(maxLimit=stack1.size())
  while not(stack1.isEmpty()):
    reversedStack.push(stack1.pop())
  return reversedStack

def reverseStackRecursively(stack, newStack = Stack()):
  '''
  Reverses a given stack using recursion
  '''
  if not(stack.isEmpty()):
    newStack.push(stack.pop())
    reverseStackRecursively(stack, newStack)
  return newStack

def createStackFromString(s):
  'Creates a stack from string while maintaining order of the string'
  assert isinstance(s, str)
  stack = Stack(maxLimit=len(s))
  for char in s:
    stack.push(char)
  return stack

if __name__ == '__main__':
  s1 = createStackFromString('abcd')
  print(reverseStack(s1))
  print(reverseStackRecursively(s1))