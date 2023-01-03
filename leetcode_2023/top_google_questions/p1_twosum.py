from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Easy
        https://leetcode.com/problems/two-sum/
        """
        d = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in d:
                d[num] = i
            else:
                return (i, d[complement])

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))