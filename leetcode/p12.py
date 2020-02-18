# @author: adnan
# 1003. Check If Word Is Valid After Substitutions (Medium)
'''
Runtime: 128 ms, faster than 29.23% of Python online submissions for Check If Word Is Valid After Substitutions.
Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Check If Word Is Valid After Substitutions.
'''
class Solution(object):
    def isValid(self, S):
        stack = []
        for char in S:
          stack.append(char)
          if len(stack) >=3 and ''.join(stack[-3:]) == 'abc':
            stack.pop()
            stack.pop()
            stack.pop()
        return not(stack)



        

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  ##### True cases
  print('------- True Cases ------- ')
  print(s.isValid("abc"))
  print(s.isValid("abcabc"))
  print(s.isValid("abcabcababcc"))
  print(s.isValid("aaabcbcbc"))
  print(s.isValid("aabcababccbc"))
  ##### False cases
  print('------- False Cases ------- ')
  print(s.isValid('ab'))
  print(s.isValid('abca'))
  print(s.isValid('abcacb'))
  print(s.isValid("aabcababccbcc"))
  