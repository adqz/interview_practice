# @author: adnan
# 1003. Check If Word Is Valid After Substitutions (Medium)
'''
Runtime: 128 ms, faster than 21.92% of Python online submissions for Check If Word Is Valid After Substitutions.
Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Check If Word Is Valid After Substitutions.
'''
class Solution(object):
    def isValid(self, S):
        """
        We are given that the string "abc" is valid.
        From any valid string V, we may split V into two pieces X and Y such that X + Y 
        (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.
        
        If for example S = "abc", then examples of valid strings are: 
        "abc", "aabcbc", "abcabc", "abcabcababcc".  
        Examples of invalid strings are: "abccba", "ab", "cababc", "bac".
        
        Return true if and only if the given string S is valid

        :type S: str
        :rtype: bool
        """
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
  