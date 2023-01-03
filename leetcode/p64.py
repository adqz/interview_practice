'''
@author: adnan
Problem 15. Three sum (Medium)


'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_hashmap = set()
        ans = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    complement = num1 + num2
                    if -complement in nums_hashmap:
                        triplet = set([num1, num2, complement])
                        if len(triplet) == 3 and triplet not in ans:
                            ans.append(list(triplet))
                    else:
                        nums_hashmap.add(complement)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))