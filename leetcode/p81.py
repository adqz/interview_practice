'''
@author: adnan
Problem 151. Reverse Words in a String

Runtime: 136 ms, faster than 27.44% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19 MB, less than 30.19% of Python3 online submissions for Contains Duplicate.
'''
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                return True
        return False
