'''
Given a list of sets, find the set that should be excluded to maximize the size of the intersection of the remaining sets

Time for intersection between sets of size m,n = O(min(m,n))

setList = [{1,2,3}, {2,3}, {1,3}, {4,5,6}, {1,2,3,4,5}]
'''

class Solution:
    '''
    The problem is solved using DP.
    Idea: If we exclude a set an index i, we need to intersect all sets on its left with all sets on the right side
    DP: Precompute left side and right side intersections

    Time: O(L) * intersection time
    Space: O(L)
    Where L = number of sets
    '''
    def __init__(self):
        self.leftToRight = dict()
        self.rightToLeft = dict()
    
    def maximizeIntersection(self, setList, verbose=False):
        # Edge case
        if len(setList) in [0, 1]:
            return None
        
        # Precompute left side and right side intersections
        self.getLeftToRightIntersections(setList)
        self.getRightToLeftIntersections(setList)
        
        maxintersectionSize = float("-inf")
        maxIndex = None
        for i in range(0, len(setList)):
            # Edge cases
            if i == 0:
                intersection = self.rightToLeft[0]
            elif i == len(setList)-1:
                intersection = self.leftToRight[len(setList)-1]
            # General case
            else:
                intersection = self.leftToRight[ i ].intersection(self.rightToLeft[ i ])
            
            intersectionSize = len(intersection)
            # Checking max size
            if intersectionSize > maxintersectionSize:
                maxintersectionSize = intersectionSize
                maxIndex = i

        if verbose:
            print('Set to exclude: ', setList[maxIndex])
            print('Size of intersection after excluding set: ', maxintersectionSize, '\n')
        
        return setList[maxIndex]
    
    def getLeftToRightIntersections(self, setList):
        '''
        For an index i, compute intersection of all sets on its left side (from 0 to i-1)
        Note: i belong to [1, len(setList)-1]
        '''
        for i in range(1, len(setList)):
            # Edge Case
            if i == 1:
                setIntersection = setList[0]
            # General Case
            else:
                previousIntersections = self.leftToRight[i-1]
                newSetToIntersect = setList[i-1]
                setIntersection = previousIntersections.intersection(newSetToIntersect)
            
            self.leftToRight[i] = setIntersection
    
    def getRightToLeftIntersections(self, setList):
        '''
        For an index i, compute intersection of all sets on its right side (from i+1 to len(setList))
        Note: i belong to [0, len(setList)-2]
        '''
        for i in range(len(setList)-2, -1, -1):
            # Edge Case
            if i == len(setList)-2:
                setIntersection = setList[-1]
            # General Case
            else:
                previousIntersections = self.rightToLeft[i+1]
                newSetToIntersect = setList[i+1]
                setIntersection = previousIntersections.intersection(newSetToIntersect)
            
            self.rightToLeft[i] = setIntersection
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximizeIntersection([{1,2,3}, {2,3}])) #{2, 3}
    print(sol.maximizeIntersection([{2,3}, {1,2,3}])) #{2, 3}
    print(sol.maximizeIntersection([{1,2,3}, {2,3}, {1,3}, {4,5,6}, {1,2,3,4,5}])) #{4, 5, 6}
    print(sol.maximizeIntersection([{1,2,3}, {2,3}, {3}, {1,2,3,4,5}])) #{3}