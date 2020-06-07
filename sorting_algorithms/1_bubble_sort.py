# O(N^2) time | O(1) space
def bubbleSort(array):
    if len(array) in [0, 1]:
        return array
    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for i in range(0, len(array) - 1 - counter):
            if array[i] > array [i+1]:
                swap(array, i, i+1)
                isSorted = False
        counter += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    print(bubbleSort([])) # []
    print(bubbleSort([2])) # [2]
    print(bubbleSort([1000,1,6])) # [1, 6, 1000]
    print(bubbleSort([5,1,4,2,3])) # [1, 2, 3, 4, 5]
    