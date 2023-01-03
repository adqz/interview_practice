class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.helper_minDistance(word1, word2, 0, 0, 0)
    
    def helper_minDistance(self, word1, word2, i1, i2, num_steps):
        # Base Case
        if word1 == word2:
            return num_steps
        
        if i1 < len(word1):
            return self.helper_minDistance(word1[:i1] + word1[i1+1:], word2, i1+1, i2, num_steps+1)
            return self.helper_minDistance(word1, word2, i1+1, i2, num_steps)
        if i2 < len(word2):
            return self.helper_minDistance(word1, word2[:i1] + word2[i1+1:], i1, i2+1, num_steps+1)
            return self.helper_minDistance(word1, word2, i1, i2+1, num_steps)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("sea", "eat")) #2