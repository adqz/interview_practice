import unittest

def quickSort(array):
    '''
    Time Complexity
    Best: O(N log(N))
    Avg: O(N log(N))
    Worst: O(N^2)
    '''
    quickSortHelper(array, 0, len(array)-1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    # Base Case
    if startIdx >= endIdx:
        return

    # Build
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, leftIdx, rightIdx)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    
    swap(array, pivotIdx, rightIdx)
    isLeftArraySmaller = (rightIdx - 1 - startIdx) < (endIdx - rightIdx+1)
    if isLeftArraySmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

class TestStringMethods(unittest.TestCase):
    def setUp(self): 
        self.testCases = [  [], 
                            [2], 
                            [1000,1,6], 
                            [5,1,4,2,3],
                        ]

        self.answers = [    [],
                            [2],
                            [1, 6, 1000],
                            [1, 2, 3, 4, 5],
                        ]

    def test_1(self):
        '''
        Edge case 1: Empty array
        '''
        ans = quickSort(self.testCases[0])
        self.assertEqual(ans, self.answers[0])
    
    def test_2(self):
        '''
        Edge case 2: Single element array
        '''
        ans = quickSort(self.testCases[1])
        self.assertEqual(ans, self.answers[1])
    
    def test_3(self):
        '''
        General case 3 and 4
        '''
        for i in range(2,4):
            ans = quickSort(self.testCases[i])
            self.assertEqual(ans, self.answers[i])

if __name__ == "__main__":
    unittest.main()
    