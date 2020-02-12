'''
@author: adnan
Problem 991. Broken Calculator
Time: O(N), Space: O(1)

Runtime: 316 ms, faster than 57.40% of Python3 online submissions for Grumpy Bookstore Owner.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.

Idea: Total number of satisfied customers can only increase, so we calculate a base value and then
calculate what is the maximum number of customer we can possibly make happy with window of size X

1. Loop over customers and keep track of satisfied, current_possible_satisfied, max_possible_satisfied
2. Move window when needed and recalculate current_possible_satisfied
3. Return satisfied + max_possible_satisfied
'''
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # 1 = grumpy, 0 = not grumpy (satisfied)
        base_satisfied, possible_satisfied, max_possible = 0, 0, 0
        i = 0
        for j in range(len(customers)):
            num_customers, state = customers[j], grumpy[j]
            # 2. Moving window
            if j - X == i:
                possible_satisfied -= customers[i] * (grumpy[i] == 1)
                i += 1
            
            # Updating base_satisfied and maximum possible customers that can be satisfied with window size of X
            base_satisfied += num_customers * (state == 0)
            possible_satisfied += num_customers * (state == 1)
            max_possible = max(max_possible, possible_satisfied)
        
        return base_satisfied + max_possible

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3))