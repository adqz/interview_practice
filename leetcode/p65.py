'''
@author: adnan
Problem 991. Broken Calculator
Time: O(logY), Space: O(1)

Runtime: 20 ms, faster than 96.80% of Python3 online submissions for Broken Calculator.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Broken Calculator.
'''
from typing import List
from collections import defaultdict
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        num_operations = 0
        while Y > X:
            num_operations += 1
            if Y%2 == 0: Y /= 2
            else: Y += 1
        
        return num_operations + int(X-Y)
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.brokenCalc(5, 8))


'''
Initial Solution - Not working
from collections import defaultdict
class Solution:
    def __init__(self):
        self.min_operations = defaultdict(lambda : float('inf')) #key = number, value = number of operations needed to reach it
    def brokenCalc(self, X: int, Y: int) -> int:
        self.min_operations[X] = 0
        self.brokenCalc_helper(X, Y)
        print(self.min_operations)
        return self.min_operations[Y]

    def brokenCalc_helper(self, X, Y):
        # Corner case: Only decrement
        if X > Y:
            self.min_operations[X] = X-Y
            return
        # Base case
        if X == Y:
            return
        # General Case
        X_decremented = X - 1
        X_doubled = X*2
        num_ops = self.min_operations[X] + 1
        print(X_doubled, X_decremented, num_ops)
        if num_ops < self.min_operations[X_decremented]:
            self.min_operations[X_decremented] = num_ops
        if num_ops < self.min_operations[X_doubled]:
            self.min_operations[X_doubled] = num_ops
        
        self.brokenCalc_helper(X_doubled, Y)    
        self.brokenCalc_helper(X_decremented, Y)

'''