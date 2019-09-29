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

def check_palindrome(instring):
  '''
  Checks whether a given string is a palindrome or not using stacks.
  Can also be done using lists
  '''
  assert isinstance(instring, str) and len(instring) > 0

  reversedString = Stack(maxLimit=len(instring))
  for char in instring:
    reversedString.push(char)
  for char in instring:
    if char != reversedString.pop():
      return False
  return True

if __name__ == '__main__':
  print(check_palindrome('madam'))
  print(check_palindrome('12321'))
  print(check_palindrome('nurses run'))
  print(check_palindrome('nurserun'))
