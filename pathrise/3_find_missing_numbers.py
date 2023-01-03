'''
Given a range between start and end and a sorted array, arr, of integer values, print the missing items from the list for the given range. 
When displaying values use shorthand hyphenated notation when possible for example 4-5 and 4-10 instead of 4,5 and 4,5,6,7,8,9,10.

Given arr=[1,3,5,7,8,9,13].

Call find_missing_nums(arr, 5, 12)  -> 6, 10-12
Call find_missing_nums(arr, 1, 5)   -> 2, 4
Call find_missing_nums(arr, 10, 13) -> 10-12

start and end are not necessarily in the array
can have negatives
start is not necessarily less than end
'''

def find_missing_nums(arr, start, end):
    # TODO: asserts and docstring
    
    if start > end:
        return -1
        
    if start < arr[0] and end < arr[0]: #checking for min
        print(f'Range = {start} - {end}')
    
    if start > arr[-1] and end > arr[-1]: #checking for min
        print(f'Range = {start} - {end}')
    
    to_compare = []
    for i in range(len(arr)):
        if start == arr[i]:
            for j in range(i, len(arr)):
                if arr[j] <= end:
                    to_compare.append(arr[j])
    
    start_to_end = set(list(range(start, end+1)))
    to_compare = set(to_compare)
    
    print(start_to_end.difference(to_compare))
    

arr=[1,3,5,7,8,9,13]
find_missing_nums(arr, 5, 12)

'''
DP

DFS BFS

Search

Sort

'''

# 5, 6, 7, 8, 9, 10, 11, 12
# 

# Time = O(end-start)
def find_missing_nums_brute(arr, 5, 12):
    set_arr = set(arr)
    for num in range(start, end+1):
        if num not in set_arr:
            print(num)
    
# Time = O(end-start * num elements in array)
def find_missing_nums_brute(arr, 5, 12):
    for num in range(start, end+1):
        if num not in arr:
            print(num)

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    
    while l+1<r:
        mid = l + (r-l)//2
        
        if arr[mid] == target:
            return True
        elif (target > arr[mid]):
            l = mid
        else:
            r = mid
    
    # Post
    if arr[l] or arr[r] == target: return True
    
    return False
    
    
# Time = O(end-start * log len(arr))
def find_missing_nums_binary_search(arr, 5, 12):
    for num in range(start, end+1):
        if not binary_search(arr, num):
            print(num)
            
            
# Time: O(n)
def printRangeWithHyphens(nums, start, end):
   next = start
   for num in nums:
       if num < start:
           continue
       if num > end:
           printNumbers(next, end)
           return
       if num > next:
           printNumbers(next, num-1)
       next = num+1

   if next <= end:
       printNumbers(next, end)

def printNumbers(start, end):
    if start==end:
        print(start)
    else:
        if start < 0:
            print('(' + str(start) + ')-', end='')
        else:
            print(str(start) + '-', end='')
        if end < 0:
            print('(' + str(end) + ')-', end='')
        else:
            print(end)