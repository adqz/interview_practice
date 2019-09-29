# @author: adnan
# Problem No. 9
class Solution(object):
    '''
    Problem: Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.
    '''
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        assert isinstance(x, int)

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
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False

        rev = self.reverse(x)
        return True if x==rev else False

s = Solution()
print(s.isPalindrome(10))