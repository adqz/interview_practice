from typing import List
class LargestNumKey(str): #inherits from str class
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(map(str, nums), key = LargestNumKey)
        return ''.join(sorted_nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10, 2])) #210