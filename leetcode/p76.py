'''
@author: adnan
Problem 441. Arranging Coins (Easy)

Runtime: 1328 ms, faster than 17.25% of Python3 online submissions for Arranging Coins.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Arranging Coins.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.arrangeCoins(0)) #0
    print(sol.arrangeCoins(5)) #2
    print(sol.arrangeCoins(6)) #3
    print(sol.arrangeCoins(8)) #3


'''
# Solution 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        row, num_rows = 1, 0
        while n>0:
            n -= row
            row += 1
            if n >= 0:
                num_rows += 1
        
        return num_rows
'''

