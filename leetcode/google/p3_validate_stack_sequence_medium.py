'''
https://leetcode.com/problems/validate-stack-sequences/submissions/

Runtime: 76 ms, faster than 52.22% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Validate Stack Sequences.
'''
from typing import List
class Solution:
    '''
    n = len(pushed)
    m = len(popped)
    Time: O(n+m)
    Space: O(n)
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for num in pushed:
            stack.append(num)
            while pop_index < len(popped) and stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        if stack == []:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])) #true
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])) #false