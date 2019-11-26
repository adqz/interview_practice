from functools import lru_cache
from collections import defaultdict
class Solution(object):
  def canPartition(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total%2 != 0:
      return False
    return self.canPartition2(tuple(nums), 0, 0, total)
  
  
  def canPartition2(self, nums, index, sums, total, Hashmap=defaultdict(bool)):
    if (index,sums) in Hashmap.keys(): #cache
      return Hashmap[(index,sums)] 
    if sums == total/2:
      return True
    if sums>total/2 or index >= len(nums):
      return False
    else:
      foundPartition = self.canPartition2(nums, index+1, sums, total) or \
        self.canPartition2(nums, index+1, sums + nums[index], total)
      Hashmap[(index,sums)] = foundPartition
      return foundPartition

if __name__ == '__main__':

  sol = Solution()
  testcase = [1,2,3,4]
  testcase = [1,5,11,5]
  ans = sol.canPartition(testcase)
  print(f'ans = {ans}')


'''
from itertools import groupby
from operator import itemgetter
class Solution(object):
  def canPartition(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) in [0,1]:
      return False
    if sum(nums)%2 != 0: #cannot split if sum is odd
      return False
    
    all_combos = ['{0:0b}'.format(i).zfill(len(nums)) for i in range(1, 2**len(nums)//2 + 1)]
    
    paired = [list(zip(combo, nums)) for combo in all_combos]
    paired = [sorted(y, key=itemgetter(0)) for y in paired]
    
    for pair in paired:
      sums = []
      for group, items in groupby(pair, key=itemgetter(0)):
        sums.append(sum(map(itemgetter(1), items)))
      if sums[0] == sums[1]:
        return True
    return False
'''