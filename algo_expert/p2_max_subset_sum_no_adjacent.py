# O(n) Time | O(1) Space
def maxSubsetSumNoAdjacent(array, index = 0, curr_sum = 0):
    # Corner Case 1
    if len(array) == 1:
        return array[0]
    # DP Case 1: index and index+1 are within bounds of array
    if index + 1 < len(array):
        # DP with Recursion
        choice_1 = array[index] + maxSubsetSumNoAdjacent(array, index+2, curr_sum)
        choice_2 = array[index+1] + maxSubsetSumNoAdjacent(array, index+3, curr_sum)
        return max(choice_1, choice_2)
    # DP Case 2: Only index is within bounds of array
    elif index < len(array):
        return curr_sum + array[index]
    # DP Case 3: Neither index, nor index+1 are within bounds of array
    else:
        return curr_sum
    

if __name__ == "__main__":
    print(maxSubsetSumNoAdjacent_alternate([1])) #1
    print(maxSubsetSumNoAdjacent_alternate([1, 15, 3])) #15
    print(maxSubsetSumNoAdjacent_alternate([1, 2, 3])) #4
    print(maxSubsetSumNoAdjacent_alternate([75, 105, 120, 75, 90, 135])) #330

# O(n) Time | O(n) Space
def maxSubsetSumNoAdjacent_alternate(array):
    # Corner cases
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    
    maxSums = array[:] #deep copy
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + maxSums[i])
    
    return maxSums[-1]