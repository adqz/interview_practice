import unittest

# O(N^2) time | O (1) space
def insertionSort(array):
    '''
    Time Complexity
    Best: O(n) - if array is already sorted
    Avg: O(N^2)
    Worst: O(N^2)
    '''
    if len(array) in [0, 1]:
        return array

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(array, j, j-1)
            j -= 1
    
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Python code to demonstrate working of unittest 

  
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
        ans = insertionSort(self.testCases[0])
        self.assertEqual(ans, self.answers[0])
    
    def test_2(self):
        '''
        Edge case 2: Single element array
        '''
        ans = insertionSort(self.testCases[1])
        self.assertEqual(ans, self.answers[1])
    
    def test_3(self):
        '''
        General case 3 and 4
        '''
        for i in range(2,4):
            ans = insertionSort(self.testCases[i])
            self.assertEqual(ans, self.answers[i])

if __name__ == "__main__":
    unittest.main()
    