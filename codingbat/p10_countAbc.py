class Solution:
    def countAbc(self, s):
        return self.helper_countAbc(s, 0, 0)
        
    def helper_countAbc(self, s, index, count):
        # Base Case
        if index + 3 > len(s):
            return count
        
        if s[index: index+3] in ['abc', 'aba']:
            count += 1
        
        return self.helper_countAbc(s, index+1, count)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAbc('abc')) #1
    print(sol.countAbc('abcxxabc')) #2
    print(sol.countAbc('abcxxaba')) #2