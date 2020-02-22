'''
@author: adnan
Problem 661. Image Smoother (Easy)

Runtime: 828 ms, faster than 40.07% of Python3 online submissions for Image Smoother.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Image Smoother.
'''
from typing import List
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        self.R, self.C = len(M), len(M[0])
        self.M = M
        ans = [[0]*self.C for _ in range(self.R)]
        for r in range(self.R):
            for c in range(self.C):
                neighbour_values = self.get_neighbour_values(r,c)
                average = int(sum(neighbour_values)/len(neighbour_values))
                ans[r][c] = average
        
        return ans

    def get_neighbour_values(self, r, c):
        neighbour_vales = [self.M[r][c]]
        for i, j in [(r, c+1), (r, c-1), (r+1, c), (r-1, c), \
                    (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]:
            if 0 <= i < self.R and 0 <= j < self.C:
                neighbour_vales.append(self.M[i][j])

        return neighbour_vales


if __name__ == "__main__":
    sol = Solution()
    print(sol.imageSmoother([[1,1,1],
                    [1,0,1],
                    [1,1,1]]))