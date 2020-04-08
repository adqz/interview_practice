def binary_search(arr, key):
    l, r = 0, len(arr)-1
    while l+1 < r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid
        else:
            r = mid
    
    # Post Processing
    if arr[l] == key: return l
    if arr[r] == key: return r

    return -1 #if not found

def binary_search_recursive(arr, key, low, high):
    # Base case 1
    if low > high:
        return -1
    
    mid = low + (high-low)//2
    # Base case 2
    if arr[mid] == key:
        return mid
    # Recursive Cases
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid+1, high)
    else:
        return binary_search_recursive(arr, key, low, mid-1)
    