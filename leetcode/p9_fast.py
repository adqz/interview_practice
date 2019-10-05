# @author: adnan
# Problem 20. Valid Parentheses (Easy)
'''
Runtime: 16 ms, faster than 84.94% of Python online submissions for Valid Parentheses.
Memory Usage: 11.6 MB, less than 100.00% of Python online submissions for Valid Parentheses.
'''
class Solution(object):
    def isValid(self, s):
        if s == '':
          return True
        stack = []
        closingBraceOf = { '(': ')', '[': ']', '{': '}'
        }
        for char in s:
          if char in ['(', '{', '[']:
            stack.append(char)
          if char in [')', '}', ']']:
            if not(stack):
              return False
            if char != closingBraceOf[stack.pop()]:
              return False

        if not(stack):
          return True
        else:
          return False
        

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
  