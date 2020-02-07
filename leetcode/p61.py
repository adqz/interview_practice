'''
@author: adnan
Problem 279. Perfect Squares (Medium)

Runtime: 204 ms, faster than 82.84% of Python3 online submissions for Perfect Squares.
Memory Usage: 13.6 MB, less than 70.00% of Python3 online submissions for Perfect Squares.
'''
from typing import List
from collections import deque
from math import sqrt, floor

class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0: return -1
        max_square = int(floor(sqrt(n)))
        perfect_squares = [num**2 for num in range(max_square+1)]
        queue = {n} # set of remainders
        
        level = 0
        while queue:
            level += 1
            next_queue = set() #creating next queue of remainders
            for remainder in queue:
                for square in perfect_squares:
                    if remainder == square:
                        return level #found the min number of squares it takes to form n!
                    elif remainder > square:
                        next_queue.add(remainder - square)
                    else:
                        break # if remainder < square, we cannot proceed
            queue = next_queue
        
        return level

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12)) #3
    print(sol.numSquares(13)) #2
    print(sol.numSquares(1)) #1
    print(sol.numSquares(-10)) #-1
    