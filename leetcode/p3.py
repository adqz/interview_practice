# @author: adnan
# Problem No. 9
class Solution(object):
    def reverse(self, x):
        sign = 1 if x>0 else -1
        rev = ''
        for n in str(abs(x)):
            rev = n + rev
        rev = sign * int(rev)
        if (rev < -(2**31) or rev > (2**31) - 1):
            return 0
        else:
            return rev
    def isPalindrome(self, x):
        if x < 0:
        	return False
        rev = self.reverse(x)
        return True if x==rev else False

s = Solution()
print(s.isPalindrome(10))