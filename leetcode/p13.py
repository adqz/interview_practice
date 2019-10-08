# ----------------------- UNSOLVED -----------------------
# @author: adnan
# Problem No. 18. 4Sum
import itertools as it
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = dict()
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum in d:
              d[sum].append((i,j))
            else:
              d[sum] = [(i,j)]
        
        ans = set()
        for key in d:
          diff = target - key
          if diff in d:
            list1, list2 = d[key], d[diff]
            # print(list1,list2)
            for (i,j) in list1:
              for (k,l) in list2:
                # print(i,j,k,l)
                if i!=k and i!=j and j!=k and j!=l:
                  combo = [nums[i], nums[j], nums[k], nums[l]]
                  combo.sort()
                  ans.add(tuple(combo))
        return list(ans)

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  # nums, target = [2, 3, 2, 2, 1], 5
  # s.fourSum(nums, target)
  print(s.fourSum([1,0,-1,0,-2,2], 0))
  # nums, target = [9, 3, 4, 5, 6, 1, 7, 4, 5, 6, 7], 22
  # s.fourSum(nums, target)


'''
import itertools as it
class Solution(object):
    def fourSum(self, nums, target):
        """
        Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
        in nums such that a + b + c + d = target? Find all unique quadruplets in the array which 
        gives the sum of target

        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combos = it.combinations(nums, 4)
        quadruplets = set()
        for c in combos:
          if sum(c) == target:
            c = tuple(sorted(c))
            quadruplets.add(c)
        # print(quadruplets)
        return [list(el) for el in quadruplets]
'''