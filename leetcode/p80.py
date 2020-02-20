'''
@author: adnan
Problem 151. Reverse Words in a String

Runtime: 28 ms, faster than 73.31% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Reverse Words in a String.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        print(words)
        stack = [words[i] for i in range(len(words)-1, -1, -1) if words[i] != '']
        reversed_s = ' '.join(stack)
        return reversed_s

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  hello world!  "))
    print(sol.reverseWords("a good   example"))