def reserve_array(arr, l, r):
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

# O(L) time | O(1) space. L = length of array
def rotate_array(arr, n):
    length = len(arr)
    # Normalizing n
    n = n%length
    # Converting negative n into positive
    if n < 0:
        n = length + n
    
    reserve_array(arr, 0, length - 1)
    reserve_array(arr, 0, n-1)
    reserve_array(arr, n, length-1)

    return arr
if __name__ == "__main__":
    print(rotate_array([1,2,3,4,5], 2)) #[4,5,1,2,3]
    print(rotate_array([1,2,3,4,5], 3)) #[3,4,5,1,2]
    print(rotate_array([1,2,3,4,5], 8)) #[3,4,5,1,2]
    print(rotate_array([1,2,3,4,5], 5)) #[1,2,3,4,5]

'''
## Solution 1
from collections import deque
def rotate_array(arr, n):
    # treat array as a stack
    n = n%len(arr)
    queue = deque([])
    for _ in range(n):
        element = arr.pop()
        queue.appendleft(element)
    
    return list(queue) + arr
'''
'''
## Solution 2
def rotate_array(arr, n):
    n = n%len(arr)
    if n < 0:
        n = len(arr) + n
    arr = list(reversed(arr))
    arr[0:n] = list(reversed(arr[0:n]))
    arr[n:] = list(reversed(arr[n:]))
    return arr
'''