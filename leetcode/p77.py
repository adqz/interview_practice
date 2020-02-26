'''
@author: adnan
Problem 436. Find Right Interval (Medium)

Runtime: 436 ms, faster than 20.78% of Python3 online submissions for Find Right Interval.
Memory Usage: 18.8 MB, less than 33.33% of Python3 online submissions for Find Right Interval.
'''
from typing import List
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 0. Corner case
        if len(intervals) <= 1:
            return [-1]
        ans = []
        interval_indices = {tuple(interval): i for i, interval in enumerate(intervals)}
        # Sort according to interval start point - O(nlog(n))
        intervals_sorted = sorted(intervals, key = lambda interval: interval[0])
        start_points = sorted([interval[0] for interval in intervals])
        for start, end in intervals:
            i = self.binary_search(start_points, target = end)
            if i == -1:
                ans.append(-1)
            else:
                index = interval_indices[tuple(intervals_sorted[i])]
                ans.append(index)
        return ans
    
    def binary_search(self, arr, target):
        if not arr:
            return -1
        l, r = 0, len(arr) - 1
        while l+1 < r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                r = mid
                # return mid
            if arr[mid] < target:
                l = mid
            else:
                r = mid
        # Post Processing
        if arr[l] == target: return l
        if arr[r] == target: return r
        if arr[r] > target: return r

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRightInterval([ [3,4], [2,3], [1,2] ])) # [-1, 0, 1]
    print(sol.findRightInterval([ [11,15], [1,3], [2,9] ])) # [-1, 0, 0]
    print(sol.findRightInterval([ [1,2] ])) # [-1]
    print(sol.findRightInterval([ [1,4], [2,3], [3,4] ])) # [-1, 2, -1]
    print(sol.findRightInterval([ [4,5],[2,3],[1,2] ])) # [-1,0,1]
    
    
'''
# Solution 1: Wrong
Time: O(n), Space: O(n)
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 0. Corner case
        if len(intervals) <= 1:
            return [-1]
        # 1. Find index of start of all intervals
        start_locations = dict()
        for i, (start, _) in enumerate(intervals):
            start_locations[start] = i
        # 2. Go through all end intervals and check in dictionary for location
        ans = []
        for _, end in intervals:
            if end in start_locations:
                ans.append(start_locations[end])
            else:
                ans.append(-1)
        
        return ans
'''

'''
Solution 2: Correct, Brute Force
Time: O(n^2), Space: O(n)
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 0. Corner case
        if len(intervals) <= 1:
            return [-1]
        ans = []
        for start_i, end_i in intervals:
            min_start_j = float('inf')
            min_start_j_index = None
            # Going through each interval
            for j, (start_j, end_j) in enumerate(intervals):
                if start_j >= end_i:
                    # Finding min start_j which is greater than end_i
                    if start_j < min_start_j:
                        min_start_j = start_j
                        min_start_j_index = j
            if min_start_j != float('inf'):
                ans.append(min_start_j_index)
            else:
                ans.append(-1)
        
        return ans
'''