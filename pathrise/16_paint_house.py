'''

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.

'''

'''
Recursion
n = 4
houses = [0, 1, 2, 3]
red = 1
blue = 2
green = 3

At index i, cost[houses[i:]] = min of
1. red + cost[houses[i+1:]]
2. blue + cost[houses[i+1:]]
3. green + cost[houses[i+1:]]

        1   2   3   4 
red.   10    
green  20
blue   30


ADNAN
Communication = 4.5/5
Problem-Solving = 4.5/5
Syntax = 3.5/5
Verification = 3/5

MIKE
Communication = 5/5
Problem-Solving = 5/5
Syntax = 3.5/5
Verification = 3/5


'''
# Time Complexity
# Recursion - O(2^n)
# DP - O(n)    
class Solution():
    def minCost(self, cost):
        if not cost:
            return 0
        self.cost = cost
        self.n = len(cost)
        self.cache = dict()
        
        min_cost = min(
                        self.getMinCost(0, 0), #red
                        self.getMinCost(0, 1), #blue
                        self.getMinCost(0, 2), #green
                        )
        return min_cost

    def getMinCost(self, curr_index, prev_color_index):
        if (curr_index, prev_color_index) in self.cache:
            return self.cache[(curr_index, prev_color_index)]
        # Base
        if curr_index == self.n-1:
            if prev_color_index == 0: #red
                return min(self.cost[curr_index][1], self.cost[curr_index][2])
            elif prev_color_index == 1: #blue
                return min(self.cost[curr_index][0], self.cost[curr_index][2])
            elif prev_color_index == 2: #green
                return min(self.cost[curr_index][0], self.cost[curr_index][1])
        
        # Recursive Case
        if prev_color_index == 0: #red
            min_cost = min(
                self.cost[curr_index][1] + self.getMinCost(curr_index+1, prev_color_index = 1),
                self.cost[curr_index][2] + self.getMinCost(curr_index+1, prev_color_index = 2)
            )
        elif prev_color_index == 1: #blue
            min_cost = min(
                self.cost[curr_index][0] + self.getMinCost(curr_index+1, prev_color_index = 0),
                self.cost[curr_index][2] + self.getMinCost(curr_index+1, prev_color_index = 2)
            )
        elif prev_color_index == 2: #green
            min_cost = min(
                self.cost[curr_index][0] + self.getMinCost(curr_index+1, prev_color_index = 0),
                self.cost[curr_index][1] + self.getMinCost(curr_index+1, prev_color_index = 1)
            ) 
        
        self.cache[(curr_index, prev_color_index)] = min_cost
        return min_cost
    
if __name__ == "__main__":
    sol = Solution()
    cost = [[17,2,17],[16,16,5],[14,3,19]]
    print(sol.minCost(cost)) #10
    