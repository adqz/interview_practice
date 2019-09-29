import itertools as it
class Solution(object):
    def twoSum(self, nums, target):
        """
        Returns a list with 2 indices of the numbers that add up to the target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert isinstance(nums, list) and len(nums)>=2
        assert isinstance(target, int)
        for n in nums:
            assert isinstance(n, int)

        d = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment not in d:
                d[num] = i
            else:
                return [d[compliment], i]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

'''
Solution 1 (Failed due to time complexity)

class Solution(object):
    def twoSum(self, nums, target):
        """
        Returns a list with 2 indices of the numbers that add up to the target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        assert isinstance(nums, list) and len(nums)>=2
        assert isinstance(target, int)
        for n in nums:
            assert isinstance(n, int)
        
        numsWithIndices = zip(range(len(nums)), nums)
        combos = it.combinations(numsWithIndices, 2)
        for combo in combos:
            if combo[0][1] + combo[1][1] == target:
                return [combo[0][0], combo[1][0]]
'''