'''
------- Start: Problem -------
We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, 
the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total
 number of blocks in such a triangle with the given number of rows.


triangle(0) → 0
triangle(1) → 1
triangle(2) → 3
------- End: Problem -------
'''
class Solution:
    def triangle(self, num_rows):
        return self.triangle_helper(num_rows, 0)
    def triangle_helper(self, curr_row, num_blocks):
        if curr_row == 0:
            return num_blocks
        else:
            return self.triangle_helper(curr_row-1, num_blocks + curr_row)

if __name__ == "__main__":
    sol = Solution()
    print(sol.triangle(0)) #0
    print(sol.triangle(1)) #1
    print(sol.triangle(2)) #3
    print(sol.triangle(4)) #10