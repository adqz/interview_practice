'''
@author: adnan
Problem 1. Two sum (Easy)

Runtime: 28 ms, faster than 98.10% of Python online submissions for Two Sum.
Memory Usage: 13.3 MB, less than 15.07% of Python online submissions for Two Sum.
'''
from typing import List
from collections import defaultdict
import itertools as it

class Solution(object):
    def twoSum(self, nums, target):
        nums_hashmap = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in nums_hashmap:
                nums_hashmap[num] = i
            else:
                return i, nums_hashmap[diff]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    