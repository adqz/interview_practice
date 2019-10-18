# @author: adnan
# Problem No. 739. Daily Temperatures (Medium)
'''
Runtime: 484 ms, faster than 25.67% of Python online submissions for Daily Temperatures.
Memory Usage: 15.3 MB, less than 34.61% of Python online submissions for Daily Temperatures.
'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        Given a list of daily temperatures T, return a list such that, for each day in the input, 
        tells you how many days you would have to wait until a warmer temperature. 
        If there is no future day for which this is possible, put 0 instead.
        For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
        your output should be [1, 1, 4, 2, 1, 1, 0, 0].
        
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
          while stack and T[i] >= stack[-1][1]:
            stack.pop()
          if stack:
            ans[i] = stack[-1][0] - i
          stack.append((i,T[i]))
          # print(stack)
        return ans


if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  T = [73, 74, 75, 71, 69, 72, 76, 73]
  print(T)
  print(s.dailyTemperatures(T))

'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = []
        for i,t in enumerate(T):
          warmerDayFound = False
          for j,u in enumerate(T[i+1:],i+1):
            if u>t:
              ans.append(j-i)
              warmerDayFound = True
              break
          if not(warmerDayFound):
            ans.append(0)
        return ans
'''