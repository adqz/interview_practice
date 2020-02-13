'''
@author: adnan
Problem Tom Sawyer paints fence

Problem: Give an integer array arr[] consisting of elements from the set {0, 1}.
The task is to print the number of ways the array can be divided into sub-arrays such that each sub-array contains exactly one 1.

Test Cases:
arr = 10101
Output = 4

The ways to divide arr are:
10|10|1
1|010|1
10|1|01
1|01|01

n = 2, arr = 00
Output = 0
The fence does not need any painting


Idea: Between 
Time: O(n^2), Space: O(n)

'''
class Solution():
    def numberOfWays(self, arr):
        n = len(arr)
        pos = [0 for _ in range(n)]

        p = 0
        for i in range(n):
            if arr[i] == 1:
                pos[p] = i+1
                p += 1
        
        # Corner case
        if p == 0: return 0
        
        num_ways = 1
        for i in range(p-1):
            num_ways *= pos[i+1] - pos[i]

        return num_ways

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfWays([1,0,1,0,1]))
