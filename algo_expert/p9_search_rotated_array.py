def binary_search_rotated(arr, key):
    l, r = 0, len(arr)-1

    while l+1 < r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        elif key >= arr[0] and key > arr[mid]:
            r = mid
        elif key <= arr[-1] and key < arr[mid]:
            l = mid
        elif arr[mid] < key:
            l = mid
        else:
            r = mid
    # Post Processing
    if arr[l] == key: return l
    if arr[r] == key: return r

    return -1

if __name__ == "__main__":
    print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 188)) #1
    print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 88)) #6
    print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 176)) #0
    print(binary_search_rotated([222, 1, 10, 63, 88, 176, 188], 222)) #0
    print(binary_search_rotated([10, 63, 88, 176, 188, 222, 1], 222)) #5
    print(binary_search_rotated([10, 63, 88, 176, 188, 222, 1], 1)) #6