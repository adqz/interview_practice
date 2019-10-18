# @author: adnan
# Problem No. 771. Jewels and Stones (Easy)
'''
Runtime: 12 ms, faster than 94.04% of Python online submissions for Jewels and Stones.
Memory Usage: 11.7 MB, less than 65.59% of Python online submissions for Jewels and Stones.
'''

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  Each character in S is a type of stone you have.  
        You want to know how many of the stones you have are also jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters. 
        Letters are case sensitive, so "a" is considered a different type of stone from "A".

        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(J.count, S))

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  J = "aA"; S = "aAAbbbb"
  print(s.numJewelsInStones(J, S))
  J = "z"; S = "ZZ"
  print(s.numJewelsInStones(J, S))

'''
Runtime: 16 ms, faster than 76.16% of Python online submissions for Jewels and Stones.
Memory Usage: 11.8 MB, less than 24.73% of Python online submissions for Jewels and Stones.
'''
  '''
  class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  Each character in S is a type of stone you have.  
        You want to know how many of the stones you have are also jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters. 
        Letters are case sensitive, so "a" is considered a different type of stone from "A".

        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for s in S:
          if s in J: counter+=1
        return counter
  '''