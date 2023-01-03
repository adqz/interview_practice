class Solution():
    '''
    [1 1 3 5 7 7 9 10 10] --> [1 3 5 7 9 10 1 10 7]
    
    [1, 3, 5, 3, 1, 1, 7, 7]
                 i  j
    last_compared = 5
    '''
    def non_repeat_sort(self, arr):
        # we don't start from 0 because that will always be correct!
        i, j = 1, 2
        # last_compared = 1
        while j < len(arr):
            # print(arr, i, j, arr[i], arr[j], last_compared)
            if arr[j] > arr[i] and arr[j] not in arr[:i]:
                # last_compared = arr[j]
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
                j = i+1
            else:
                j += 1
        return arr

if __name__ == "__main__":
    sol = Solution()
    print(sol.non_repeat_sort([1, 1, 1, 3, 3, 5, 7, 7])) #[1,3,5,7, ...]
    print(sol.non_repeat_sort([1, 1, 1, 3, 5, 7, 7, 9, 10, 10])) #[1,3,5,7,9,10 ...]
