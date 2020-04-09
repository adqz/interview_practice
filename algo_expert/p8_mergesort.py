from collections import deque
# Best, Avg, Worst --> O(logn) time | O(logn) space
def mergeSort(array):
    if not array:
        return []
    if len(array) == 1:
        return array

    mid = len(array)//2
    half1, half2 = array[:mid], array[mid:]
    
    return merge(mergeSort(half1), mergeSort(half2))

def merge(arr1, arr2):
    result = []
    arr1, arr2 = deque(arr1), deque(arr2)
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            number = arr1.popleft()
            result.append(number)
        else:
            number = arr2.popleft()
            result.append(number)

    while arr1: result.append(arr1.popleft())
    while arr2: result.append(arr2.popleft())
    
    return result

if __name__ == "__main__":
    print(mergeSort([1,2,3,5,4])) #[1,2,3,4,5]
    print(mergeSort([1])) #[1]
    print(mergeSort([4,2]))