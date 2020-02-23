'''
------- Start: Problem -------
Given a non-negative int n, return the sum of its digits recursively (no loops). 
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) 
by 10 removes the rightmost digit (126 / 10 is 12).
------- End: Problem -------

sumDigits(126) = 9
sumDigits(49) = 13
sumDigits(12) = 3
'''
class Solution:
    def sumDigit(self, num, curr_sum=0):
        if num // 10 == 0:
            return curr_sum + num
        else:
            rightmost_digit = num%10
            return self.sumDigit(num//10, curr_sum+rightmost_digit)

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumDigit(123)) #6
    print(sol.sumDigit(49)) #13
    print(sol.sumDigit(12)) #3
    print(sol.sumDigit(10)) #1
    print(sol.sumDigit(0)) #0