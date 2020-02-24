'''
@author: adnan
Problem 541. Reverse String II (Easy)

Runtime: 40 ms, faster than 50.01% of Python3 online submissions for Reverse String II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse String II.
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s:
            return s
        
        ans = ''
        reverse_str, not_reverse_str = '', ''
        count = 0
        j = 0
        i = j + 2*k
        while i <= len(s) or j < len(s):
            if count < k:
                reverse_str += s[j]
                j += 1
                count += 1
                continue
            else:
                try:
                    not_reverse_str = s[j:i]
                    ans += reverse_str[::-1] + not_reverse_str
                    reverse_str, not_reverse_str = '', ''
                    j = i
                    i = j + 2*k
                    count = 0
                except IndexError:
                    break
        # Post processing
        if len(s) - j < k:
            ans += reverse_str[::-1]
        if len(s) - j > k:
            ans += reverse_str[::-1] + s[j+k:]
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseStr("abcdefghij", k=2)) #bacd