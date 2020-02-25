'''
@author: adnan
Problem 409. Longest Palindrome (Easy)

Runtime: 28 ms, faster than 81.47% of Python3 online submissions for Longest Palindrome.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        char_count = Counter(s)
        palindrome_length = 0
        for v in char_count.values():
            palindrome_length += v//2 * 2
            if palindrome_length %2 == 0 and v%2 == 1:
                palindrome_length += 1
        
        return palindrome_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abccccdd")) #7
    print(sol.longestPalindrome("ccccdd")) #6
    print(sol.longestPalindrome("Bccdd")) #5