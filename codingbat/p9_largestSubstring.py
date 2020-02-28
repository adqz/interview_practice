class Solution:
    def strDist(self, s, sub):
        return self.helper_strDist(s, sub, 0, False, 0, float('-inf'))
    
    def helper_strDist(self, s, sub, index, started, start_index, max_len):
        # Base Case
        if index + len(sub) > len(s):
            if started:
                return max(max_len, len(sub))
            else:
                return 0
        
        # Recursive Case
        if s[index: index+len(sub)] == sub:
            if not started:
                started = True
                start_index = index
            else:
                curr_len = index + len(sub) - start_index
                max_len = max(max_len, curr_len)

        return self.helper_strDist(s, sub, index+1, started, start_index, max_len)

if __name__ == "__main__":
    sol = Solution()
    print(sol.strDist("catcowcat", "abc")) #0
    print(sol.strDist("catcowcat", "cat")) #9
    print(sol.strDist("catcowcat", "cow")) #3
    print(sol.strDist("cccatcowcatxx", "cat")) #9