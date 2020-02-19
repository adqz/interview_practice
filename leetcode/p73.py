'''
@author: adnan
Problem 48. Rotate Image (Medium)

Runtime: 32 ms, faster than 74.43% of Python3 online submissions for Rotate Image.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate Image.
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        # 1. Store columns
        all_columns = []
        for c in range(C):
            column = []
            for r in range(R-1, -1, -1): #indexing in reverse
                column.append(matrix[r][c])
            all_columns.append(column)
        
        # 2. Rewrite rows
        for r in range(R):
            matrix[r] = all_columns[r]


if __name__ == "__main__":
    sol = Solution()
    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
             ]
    print(sol.rotate(matrix))

    matrix = [
                [ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]
             ]
    print(sol.rotate(matrix))