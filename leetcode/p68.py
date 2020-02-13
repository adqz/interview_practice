'''
@author: adnan
Problem 300. Longest Increasing Subsequence (Medium)

Runtime: 1152 ms, faster than 45.03% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.

Idea: DP, bottom up approach
Time: O(n^2), Space: O(n)

'''
from typing import List
from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = [1 for _ in range(len(nums))]
        for j in range(1, len(nums)):
            max_len = cache[j]
            for i in range(0,j):
                if nums[j] > nums[i]:
                    curr_len = cache[i] + 1
                    max_len = max(curr_len, max_len)
            cache[j] = max_len
        
        return max(cache)

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([-1, 3, 4, 5, 2, 2, 2, 2]))
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    
                
