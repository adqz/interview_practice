# O(max(m,n,p)) time | O(1) space. Here m,n,p = length of arr1, arr2, arr3
def find_least_common_number(arr1, arr2, arr3):
    i, j, k = 0, 0, 0

    while (i < len(arr1) and j < len(arr2) and k < len(arr3)):
        # Base case
        if arr1[i] == arr2[j] == arr3[k]:
            return arr1[i]
        # Incrementing pointers for each array
        if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        elif arr3[k] <= arr1[i] and arr3[k] <= arr2[j]:
            k += 1
    return -1

if __name__ == "__main__":
    print(find_least_common_number([6, 7, 10, 25], [0, 4, 5, 6, 7, 10, 25], [1, 6, 10, 4])) #6
    print(find_least_common_number([6, 7, 10, 25], [0, 4, 5, 6, 7, 10, 25], [1, 9, 4])) #-1