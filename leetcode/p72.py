'''
@author: adnan
Problem 202. Happy Number (Easy)

Runtime: 20 ms, faster than 99.44% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.
'''
class Solution:
    '''
    Time: O(?)
    Space: O(1) + O(?)
    '''
    def isHappy(self, n: int) -> bool:
        cache_squares = dict()
        visited = set()
        summ = 0
        while summ != 1:
            if n not in visited:
                visited.add(n)
            
            n = str(n)
            summ = 0
            for digit in n:
                if digit in cache_squares:
                    summ += cache_squares[digit]
                else:
                    cache_squares[digit] = int(digit)**2
                    summ += cache_squares[digit]
            
            if summ == 1:
                return True
            if summ in visited:
                return False
            
            n = summ

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(100)) #True
    print(sol.isHappy(19)) #True