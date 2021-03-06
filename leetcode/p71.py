'''
@author: adnan
Problem 697. Degree of an Array (Easy)

Time Limit exceeded. Try again
Memory Limit exceeded. Try again
'''
from collections import Counter
from typing import List
class Solution:
    def __init__(self):
        self.cache = dict()
    
    def get_degree(self, arr):
        arr = tuple(arr)
        if arr in self.cache:
            degree = self.cache[arr]
        else:    
            count = Counter(arr)
            degree = max(count.values())
            self.cache[arr] = degree
        return degree

    def findShortestSubArray(self, nums: List[int]) -> int:
        # 0. Corner cases
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        # 1. Calculating degree of array
        degree_nums = self.get_degree(nums)
        # 2. Finding least length contiguous where degree(sub array) == degree(nums)
        i, j = 0, len(nums)
        min_len = float('inf')
        while j>i: #revisit
            flag = False
            if self.get_degree(nums[i+1:j]) == degree_nums:
                i += 1
                flag = True
            if self.get_degree(nums[i:j-1]) == degree_nums:
                j -= 1
                flag = True
            if not flag:
                break

        return j-i

if __name__ == '__main__':
    sol = Solution()
    print(sol.findShortestSubArray([1, 2, 2, 3, 1])) #2 
    print(sol.findShortestSubArray([1,2,2,3,1,4,2])) #6

'''
class Solution:
    # Brute Force
    def get_degree(self, arr):
        count = Counter(arr)

        return max(count.values())

    def findShortestSubArray(self, nums: List[int]) -> int:
        # 0. Corner cases
        if len(nums) == 1:
            return 1
        # 1. Calculating degree of array
        degree_nums = self.get_degree(nums)
        # 2. Finding least length contiguous where degree(sub array) == degree(nums)
        i, j = 0, len(nums)
        min_len = float('inf')
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)+1):
                sub_array = nums[i:j]
                if self.get_degree(sub_array) == degree_nums:
                    curr_len = len(sub_array)
                    if curr_len < min_len:
                        min_len = curr_len
        
        return min_len
'''