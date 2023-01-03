class Solution:
    r2i_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    def romanToInt(self, s: str) -> int:
        """Easy
        https://leetcode.com/problems/roman-to-integer/
        """
        number = 0
        for i, char in enumerate(s):
            if i < len(s) - 1:
                next_char = s[i+1]
                if (char == "I" and next_char in {"V", "X"}) or\
                (char == "X" and next_char in {"L", "C"}) or\
                    (char == "C" and next_char in {"D", "M"}):
                    number -= self.r2i_map[char]
                else:
                    number += self.r2i_map[char]
            else:
                number += self.r2i_map[char]
        
        return number

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt("XL"))  # 40
print(s.romanToInt("CD"))  # 400
print(s.romanToInt("MCMXCIV"))  # 1994 = 1000 - 100 + 1000 - 10 + 100 - 1 + 4 = 1994