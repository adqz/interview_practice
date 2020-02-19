'''
@author: adnan
Problem 59. Spiral Matrix II (Medium)


'''
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        max_R, max_C = n, n
        r, c = 0, 0
        curr_num = 1
        spiral = [[0]*n for _ in range(n)] #initializing spiral matrix
        
        while curr_num <= n**2 + 1:
            last_c = c
            while c < max_C:
                spiral[r][c] = curr_num
                curr_num += 1
                c += 1
            c -= 1
            last_r = r
            print(spiral)
            while r < max_R-1:
                r += 1
                print(r,c)
                spiral[r][c] = curr_num
                curr_num += 1
            max_C, max_R = c-1, r-1
            
            while c > last_c:
                c -= 1
                spiral[r][c] = curr_num
                curr_num += 1
            while r > last_r:
                r -= 1
                spiral[r][c] = curr_num
                curr_num += 1
        
        return spiral

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(3))
