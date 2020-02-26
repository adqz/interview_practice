'''
@author: adnan
Problem 268. Missing Number (Easy)

Runtime: 136 ms, faster than 84.53% of Python3 online submissions for Missing Number.
Memory Usage: 14.5 MB, less than 12.90% of Python3 online submissions for Missing Number.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            