class Solution:
    '''
    Given an array of ints, compute recursively if the array contains somewhere a value 
    followed in the array by that value times 10. We'll use the convention of considering only 
    the part of the array that begins at the given index. In this way, a recursive call can 
    pass index+1 to move down the array. The initial call will pass in index as 0.

    array220([1, 2, 20], 0) → true
    array220([3, 30], 0) → true
    array220([3], 0) → false
    '''
    def array220(self, arr, index):
        # Base Case
        if index == len(arr)-1:
            return False
        if arr[index] * 10 == arr[index+1]:
            return True
        # Recursive Case
        return self.array220(arr, index+1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.array220([3, 30], 0)) #True
    print(sol.array220([1, 2, 20], 0)) #True
    print(sol.array220([1, 2], 0)) #False
    print(sol.array220([1], 0)) #False