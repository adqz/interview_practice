# O(logn) time | O(1) space
def find_low_index(arr, key):
    l, r = 0, len(arr) - 1
    while l+1 < r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            r = mid
        elif arr[mid] < key:
            l = mid
        else:
            r = mid
    # Post Processing
    if arr[l] == key: return l
    if arr[r] == key: return r

    return -1

# O(logn) time | O(1) space
def find_high_index(arr, key):
    l, r = 0, len(arr) - 1
    while l+1 < r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            l = mid
        elif arr[mid] < key:
            l = mid
        else:
            r = mid
    # Post Processing
    if arr[r] == key: return r
    if arr[l] == key: return l
    
    return -1

if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    print(find_low_index(arr, 1), find_high_index(arr, 1)) # 0, 2
    print(find_low_index(arr, 7), find_high_index(arr, 7)) # -1, -1
    print(find_low_index(arr, 1), find_high_index(arr, 1)) # 0, 2
    print(find_low_index(arr, 6), find_high_index(arr, 6)) # 18, 23