# O(n) time | O(1) space
def move_zeros_to_left(arr):
    read_index, write_index = len(arr)-1, len(arr)-1
    # Shifting all non 0 numbers to the right
    while read_index >= 0:
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index -= 1
        read_index -= 1
    # Writing 0's to the beginning of arr
    while write_index >= 0:
        arr[write_index] = 0
        write_index -= 1
    return arr

if __name__ == "__main__":
    print(move_zeros_to_left([1,10,20,59,63,88])) #[1,10,20,59,63,88]
    print(move_zeros_to_left([1,10,20,0,59,63,0,88,0])) #[0,0,0,1,10,20,59,63,88]
    print(move_zeros_to_left([1,10,20,0,59,63,0,88])) #[0,0,1,10,20,59,63,88]

'''
## Solution 1
def reverse_array(arr, l, r):
    # Reverses in place
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

# O(n*k) time | O(1) space, n = len(arr) and k = number of zeros
def move_zeros_to_left(arr):
    pointer_start = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            reverse_array(arr, pointer_start, i)
            pointer_start += 1
            reverse_array(arr, pointer_start, i)
        i += 1
    return arr

'''