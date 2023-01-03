'''

https://docs.google.com/document/d/1rdCD3-U6Gq_vU0BTIDZqavoA-SxEaM16vKND1gmssYw/edit

Triplets that sum to zero: Given an array of distinct elements. 
The task is to find triplets in the array whose sum is zero.
Question Description

Find all 3 integers in the array sum to 0.
[-3,3,0,2,-2,1] -> [[-3, 3, 0], [0, 2, -2], … ]

Examples
[-3,3,0,2] -> [[-3,3,0], …, ]
[1,2,3,4] -> []
# Assuming repetitions is allowed
[0,-1,2] -> [[0, 0, 0], [-1, -1, 2]]




Constraints

1. Input of integers 
2. Distinct elements
3. Array might not be sorted
4. Output: list of lists , all of them should sum to zero : you are allowed to use elements, more than once!

[-3,3,0,2,-2,1] 

Ideas
1. Brute force - Generate all possible 3 pairs and check which ones sum to 0. Time: O(n^3)
2. Hash table - save time by saving elements of the array. Time: O(n^2) Space: O(n)
3. Sort

'''

def tiplets_sum_to_zero(arr):
    """doc"""
    ans = set()
    arr_dict = {num:index for (index, num) in enumerate(arr)} 
    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr):
            if i == j:
                continue
            complement = -(num1+num2)
            if complement in arr_dict:
                if arr_dict[complement] in {i,j}:
                    continue
                ans_to_add = tuple(sorted((num1, num2, complement)))
                ans.add(ans_to_add)
    return [list(a) for a in ans ]

# https://leetcode.com/problems/3sum/

# Test Cases
arr = [-3,3,0,2,-2,1]
print(tiplets_sum_to_zero(arr))
arr = [0,2,-2]
print(tiplets_sum_to_zero(arr))
arr = [-3,0]
print(tiplets_sum_to_zero(arr))
arr = [-3,3]
print(tiplets_sum_to_zero(arr))

