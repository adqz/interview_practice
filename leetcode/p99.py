'''
Runtime: 44 ms, faster than 79.89% of Python3 online submissions for Ransom Note.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ransom Note.
'''
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_count_ransom = Counter(ransomNote)
        letters_count_magazine = Counter(magazine)

        for letter, count in letters_count_ransom.items():
            if letter not in letters_count_magazine:
                return False
            if letters_count_magazine[letter] < count:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b")) # false
    print(sol.canConstruct("aa", "ab")) # false
    print(sol.canConstruct("aa", "aab")) # true
