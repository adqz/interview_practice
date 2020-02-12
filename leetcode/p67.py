'''
@author: adnan
Problem 53. Maximum Subarray
Time: O(n), Space: O(n)

Not leetcode.
Max string weight problem - https://www.geeksforgeeks.org/maximum-weight-transformation-of-a-given-string/
'''
from collections import defaultdict
class Solution:
    def maxStringWeight_helper(self, string, curr_pos, n, cache):
        #TODO: asserts and docstring
        # Base case
        if curr_pos >= n:
            return 0
        # Using cache if valid
        if cache[curr_pos] != -1:
            return cache[curr_pos]
        
        weight = 1 + self.maxStringWeight_helper(string, curr_pos + 1, n, cache) #base weight
        
        if curr_pos + 1 < n:
            if string[curr_pos] != string[curr_pos+1]:
                weight = max(4 + self.maxStringWeight_helper(string, curr_pos + 2, n, cache), weight)
            else:
                weight = max(3 + self.maxStringWeight_helper(string, curr_pos + 2, n, cache), weight)
        
        cache[curr_pos] = weight
        return weight
    
    def maxStringWeight(self, string):
        cache = defaultdict(lambda: -1)
        max_weight = self.maxStringWeight_helper(string, 0, len(string), cache)
        
        return max_weight


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxStringWeight('AA')) #3
    print(sol.maxStringWeight('ABB')) #5
    
