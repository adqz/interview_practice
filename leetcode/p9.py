# @author: adnan
# Problem 20. Valid Parentheses (Easy)

class Solution(object):
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
        determine if the input string is valid.

        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        
        Note that an empty string is also considered valid.
        
        :type s: str
        :rtype: bool
        """
        '''
        DS: Stack
        Pseudocode:
        1. Take out a character and add it to the stack if its an opening bracket
        2. If its a closing bracket, peek and see if the last element is the respective opening bracket
        3. If (2) is True, pop the element. Else, return false
        4. Loop until all characters are parsed
        5. If all characters are parsed and stack is empty, return True. Else False
        
        '''
        # assert isinstance(s, str)
        if s == '':
          return True
        stack = Stack(maxLimit=len(s))
        closingBraceOf = {
          '(': ')',
          '[': ']',
          '{': '}'
        }
        for char in s:
          if char in ['(', '{', '[']:
            stack.push(char)
          if char in [')', '}', ']']:
            if stack.size() == 0:
              return False
            if char != closingBraceOf[stack.pop()]:
              return False

        if stack.size() == 0:
          return True
        else:
          return False
        



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
  # ------ Test Cases ------
  s = Solution()
  ##### True cases
  print('------- True Cases ------- ')
  print(s.isValid(''))
  print(s.isValid('()'))
  print(s.isValid('()[]{}'))
  print(s.isValid('([]{})'))
  print(s.isValid('((((([])))))'))
  ##### False cases
  print('------- False Cases ------- ')
  print(s.isValid('('))
  print(s.isValid(']'))
  print(s.isValid('([)'))
  print(s.isValid('((((([]))))'))
  print(s.isValid(']()]'))
  print(s.isValid('}])'))
  print(s.isValid('([}])'))
  print(s.isValid('{{{)]}}}'))
  