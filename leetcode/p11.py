# @author: adnan
# 921. Minimum Add to Make Parentheses Valid (Medium)
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        Given a string S of '(' and ')' parentheses, we add the minimum number of 
        parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses 
        string is valid.

        Formally, a parentheses string is valid if and only if:

        1. It is the empty string, or
        2. It can be written as AB (A concatenated with B), where A and B are valid strings, or
        3. It can be written as (A), where A is a valid string.
        
        Given a parentheses string, return the minimum number of parentheses we must add to 
        make the resulting string valid.


        :type S: str
        :rtype: int
        """
        stack = []
        for char in S:
          if char == '(':
            stack.append(char)
          if char == ')':
            if len(stack):
              if stack[-1] == '(':
                stack.pop()
              else:
                stack.append(char)
            else:
              stack.append(char)
        return len(stack)

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  print(s.minAddToMakeValid("())")) # 1
  print(s.minAddToMakeValid("(((")) # 3
  print(s.minAddToMakeValid("()")) # 0
  print(s.minAddToMakeValid("()))((")) # 4
  print(s.minAddToMakeValid("(((()))))")) # 1
  print(s.minAddToMakeValid(")))()(")) # 4