'''
@author: adnan
Problem 22. Generate Parentheses (Medium)

Runtime: 36 ms, faster than 34.95% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.3 MB, less than 75.56% of Python3 online submissions for Generate Parentheses.
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.valid_parentesis = set()
        self.helper_generatePatenthesis(n, '(', 1, 0)

        return self.valid_parentesis

    def helper_generatePatenthesis(self, n, current, open, close):
        if open == n and close == n:
            self.valid_parentesis.add(current)
        
        if open < n:
            self.helper_generatePatenthesis(n, current + '(', open + 1, close)

        if close < open and close < n:
            self.helper_generatePatenthesis(n, current + ')', open, close + 1)
        
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
