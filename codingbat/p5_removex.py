class Solution:
    '''
    Given a string, compute recursively a new string where all the 'x' chars have been removed.
    noX("xaxb") → "ab"
    noX("abc") → "abc"
    noX("xx") → ""
    '''
    def noX(self, s, i=0, ans = ''):
        if i == len(s):
            return ans
        
        if s[i] != 'x':
            ans += s[i]
        
        return self.noX(s, i+1, ans)

if __name__ == "__main__":
    sol = Solution()
    print(sol.noX('axb')) #'ab'
    print(sol.noX('xaxbx')) #'ab'
    print(sol.noX('xx')) #''