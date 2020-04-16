# O(n^2) time | O(1) space
def insertionSort(array):
    # Edge case
    if not array:
        return []
    # Regular case
    for sorted_barrier in range(0, len(array)-1):
        i = sorted_barrier
        j = i+1
        # Sorting all elements before sorted_barrier
        while (i >= 0 and j >= 0) and array[j] < array[i]:
            array[j], array[i] = array[i], array[j]
            i -= 1
            j -= 1
            
    return array

if __name__ == "__main__":

    print(insertionSort([])) #[]
    print(insertionSort([4])) #[4]
    print(insertionSort([8,5,2,6,9,3])) #[2,3,5,6,8,9]