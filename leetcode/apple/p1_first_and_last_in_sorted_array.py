'''
@author: adnan
Problem 34. Find First and Last Position of Element in Sorted Array (Medium)

Runtime: 88 ms, faster than 67.31% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.binary_search_first(nums, target)
        last = self.binary_search_last(nums, target)

        return [first, last]
        
        
    def binary_search_first(self, arr, target):
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                r = mid
            elif arr[mid] < target:
                l = mid
            else:
                r = mid
        
        # Post Processing
        if arr[l] == target: return l
        if arr[r] == target: return r
        return -1

    def binary_search_last(self, arr, target):
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                l = mid
            elif arr[mid] < target:
                l = mid
            else:
                r = mid
        
        # Post Processing
        if arr[r] == target: return r #need to check right before left to find last!
        if arr[l] == target: return l
        return -1


if __name__ == "__main__":
    sol = Solution()
    # print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8)) #[3, 4]
    # print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6)) #[-1, -1]
    print(sol.searchRange(nums = [2,2], target = 2)) # [0,1]