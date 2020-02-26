'''
@author: adnan
Problem 739. Daily Temperatures (Medium)

Runtime: 492 ms, faster than 76.45% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.6 MB, less than 86.84% of Python3 online submissions for Daily Temperatures.
'''
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) #[1, 1, 4, 2, 1, 1, 0, 0]
