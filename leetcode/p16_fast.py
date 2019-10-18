# @author: adnan
# Problem No. 739. Daily Temperatures (Medium)
'''
Runtime: 436 ms, faster than 76.52% of Python online submissions for Daily Temperatures.
Memory Usage: 15.3 MB, less than 30.77% of Python online submissions for Daily Temperatures.
'''
class Solution(object):
    def dailyTemperatures(self, T):
        ans, stack = [0] * len(T), []
        for i in range(len(T)-1, -1, -1):
          while stack and T[i] >= T[stack[-1]]:
            stack.pop()
          if stack:
            ans[i] = stack[-1] - i
          stack.append(i)
        return ans


if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  T = [73, 74, 75, 71, 69, 72, 76, 73]
  print(T)
  print(s.dailyTemperatures(T))