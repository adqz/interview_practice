# O(logn) time | O(1) Space
def binary_search_rotated(arr, key):
    l, r = 0, len(arr)-1

    while l+1 < r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        # Check if left half is sorted and key falls in that range
        if arr[l] <= arr[mid] and arr[l] <= key < arr[mid]:
            r = mid
        # Check if right half is sorted and key falls in that range
        elif arr[r] >= arr[mid] and arr[mid] < key <= arr[r]:
            l = mid
        ### Cases for messed up order caused by rotation
        # Check if arr from [l,r] is sorted but key is greater than right end
        elif arr[l] <= arr[mid] <= arr[r] and key > arr[r]:
            l = mid
        # At this point key > arr[mid] but then the right most element is less than
        # the middle element, so we set left to mid
        elif arr[r] <= arr[mid]:
            l = mid
        # At this point key < arr[mid] but then the left most element is greater than
        # the middle element, so we set right to mid
        elif arr[l] >= arr[mid]:
            r = mid

    # Post Processing
    if arr[l] == key: return l
    if arr[r] == key: return r

    return -1

if __name__ == "__main__":
    # print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 188)) #1
    # print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 88)) #6
    # print(binary_search_rotated([176, 188, 222, 1, 10, 63, 88], 176)) #0
    # print(binary_search_rotated([222, 1, 10, 63, 88, 176, 188], 222)) #0
    print(binary_search_rotated([10, 63, 88, 176, 188, 222, 1], 222)) #5
    print(binary_search_rotated([10, 63, 88, 176, 188, 222, 1], 1)) #6