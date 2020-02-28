class Solution:
    def strCopies(self, s, sub, n):
        ans = self.helper_strCopies(s, sub, n, 0, 0)
        return ans

    def helper_strCopies(self, s, sub, n, index, num_copies):
        # Base Case
        if index + len(sub) > len(s):
            return n == num_copies
        # Recursive Case
        if s[index:index + len(sub)] == sub:
            num_copies += 1
        
        return self.helper_strCopies(s, sub, n, index+1, num_copies)


if __name__ == "__main__":
    sol = Solution()
    print(sol.strCopies("catcowcat", "cat", 2)) #True
    print(sol.strCopies("catcowcat", "cow", 2)) #False
    print(sol.strCopies("catcowcat", "cow", 1)) #True
