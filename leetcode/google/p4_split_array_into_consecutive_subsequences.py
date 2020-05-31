from typing import List
from collections import deque
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remainderQueue = deque([])
        numsQueue = deque(nums)
        # Initializing subsequence
        currSubsequence = [numsQueue.popleft()]
        
        while numsQueue:
            currNumber = numsQueue.popleft()
            if currNumber == currSubsequence[-1] + 1:
                currSubsequence.append(currNumber)
            elif currNumber == currSubsequence[-1]:
                remainderQueue.append(currNumber)
            else:
                return False
            
            if not numsQueue:
                if len(currSubsequence) < 3:
                    return False
                numsQueue = remainderQueue
                # Initializing subsequence
                if numsQueue:
                    currSubsequence = [numsQueue.popleft()]
        
        if len(currSubsequence) < 3:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPossible([1,2,3,3,4,4,5,5])) #true
    print(sol.isPossible([1,2,3,3,4,5])) #true
    print(sol.isPossible([1,2,3,4,4,5])) #false