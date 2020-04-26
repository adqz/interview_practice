'''
Runtime: 68 ms, faster than 29.06% of Python3 online submissions for Paint House.
Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Paint House.

@author: adnan
Problem 256. Paint House (Easy)
'''
# Time Complexity
# Recursion - O(2^n)
# DP - O(n)    
class Solution():
    RED = 0
    BLUE = 1
    GREEN = 2
    def minCost(self, cost):
        if not cost:
            return 0
        self.cost = cost
        self.n = len(cost)
        self.cache = dict()
        
        min_cost = min(
                        self.getMinCost(0, self.RED),
                        self.getMinCost(0, self.BLUE),
                        self.getMinCost(0, self.GREEN),
                        )
        return min_cost

    def getMinCost(self, i, prev_color):
        if (i, prev_color) in self.cache:
            return self.cache[(i, prev_color)]
        # Base
        if i == self.n - 1:
            if prev_color == self.RED: #red
                return min(self.cost[i][self.BLUE], self.cost[i][self.GREEN])
            elif prev_color == self.BLUE: #blue
                return min(self.cost[i][self.RED], self.cost[i][self.GREEN])
            elif prev_color == 2: #green
                return min(self.cost[i][self.RED], self.cost[i][self.BLUE])
        
        # Recursive Case
        if prev_color == self.RED: #red
            min_cost = min(
                self.cost[i][self.BLUE] + self.getMinCost(i+1, self.BLUE),
                self.cost[i][self.GREEN] + self.getMinCost(i+1, self.GREEN)
            )
        elif prev_color == self.BLUE: #blue
            min_cost = min(
                self.cost[i][self.RED] + self.getMinCost(i+1, self.RED),
                self.cost[i][self.GREEN] + self.getMinCost(i+1, self.GREEN)
            )
        elif prev_color == self.GREEN: #green
            min_cost = min(
                self.cost[i][self.RED] + self.getMinCost(i+1, self.RED),
                self.cost[i][self.BLUE] + self.getMinCost(i+1, self.BLUE)
            ) 
        # Store in cache
        self.cache[(i, prev_color)] = min_cost
        
        return min_cost
    
if __name__ == "__main__":
    sol = Solution()
    cost = [[17,2,17],[16,16,5],[14,3,19]]
    print(sol.minCost(cost)) #10
    