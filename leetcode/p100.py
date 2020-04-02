'''
@author: adnan
Problem 58. Length of Last Word (Easy)

Runtime: 16 ms, faster than 99.56% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Length of Last Word.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        if len(set(s)) == 1 and s[0] == ' ':
            return 0
        
        return len(s.split()[-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord('Hi World')) #5
    print(sol.lengthOfLastWord('')) #0
    print(sol.lengthOfLastWord('Hi')) #2