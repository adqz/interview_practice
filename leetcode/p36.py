'''
@author: adnan
Problem No. 454. 4Sum II (Medium)

Runtime: 312 ms, faster than 56.68% of Python3 online submissions for 4Sum II.
Memory Usage: 33.5 MB, less than 100.00% of Python3 online submissions for 4Sum II.
'''
from collections import defaultdict
from typing import List
class Solution:
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    if len(A) == 0: #corner case
      return 0
    hash_map = defaultdict(int)
    for a in A:
      for b in B:
        hash_map[a+b] += 1
    
    count = 0
    for c in C:
      for d in D:
        if -c-d in hash_map.keys():
          count += hash_map[-c-d] #add number of occurences of (-c-d) to count
    return count

if __name__ == '__main__':

  sol = Solution()
  A = [ 1, 2]
  B = [-2,-1]
  C = [-1, 2]
  D = [ 0, 2]
  ans = sol.fourSumCount(A,B,C,D)
  print(f'ans = {ans}')
  A = [0,1,-1]
  B = [-1,1,0]
  C = [0,0,1]
  D = [-1,1,1]
  ans = sol.fourSumCount(A,B,C,D)
  print(f'ans = {ans}')

'''
from typing import List
class Solution:
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    if len(A) == 0:
      return 0
    self.indices_seen = []
    return len(set(self.isSumZero(A,B,C,D,0,0,0,0)))
  
  def isSumZero(self,A,B,C,D,i,j,k,l):
    if (i,j,k,l) in self.indices_seen: #caching
      return []
    elif any(el>=len(A) for el in [i,j,k,l]): #base case 1: if index exceeds all elements
      return []
    elif A[i] + B[j] + C[k] + D[l] == 0: #base case 2: answer found
      return [(i,j,k,l)]
    else: #recursive step
      self.indices_seen.append((i,j,k,l))
      return self.isSumZero(A,B,C,D,i+1,j,k,l) + self.isSumZero(A,B,C,D,i,j+1,k,l) + \
              self.isSumZero(A,B,C,D,i,j,k+1,l) + self.isSumZero(A,B,C,D,i,j,k,l+1)
'''