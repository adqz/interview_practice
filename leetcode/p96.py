'''
@author: adnan
Problem 219. Contains Duplicate II (Easy)

Runtime: 84 ms, faster than 98.12% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 20.5 MB, less than 62.50% of Python3 online submissions for Contains Duplicate II.
'''
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, num in enumerate(nums):
            if num in d and abs(i - d[num]) <= k:
                return True
            else:
                d[num] = i
        
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) #True
    print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)) #True
    print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)) #False