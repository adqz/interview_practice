'''
@author: adnan
Problem 436. Find Right Interval (Medium)

'''
from typing import List
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


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRightInterval([ [3,4], [2,3], [1,2] ])) # [-1, 0, 1]
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