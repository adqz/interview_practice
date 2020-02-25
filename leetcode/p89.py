'''
@author: adnan
Problem 537. Complex Number Multiplication (Medium)

Runtime: 28 ms, faster than 63.41% of Python3 online submissions for Complex Number Multiplication.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Complex Number Multiplication.
'''
import cmath
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        real_a, imag_a = a.split('+')
        real_b, imag_b = b.split('+')

        a = complex(int(real_a), int(imag_a[:-1]))
        b = complex(int(real_b), int(imag_b[:-1]))
        ans = a*b
        real_ans, imag_ans = str(int(ans.real)), str(int(ans.imag))

        return real_ans + '+' +imag_ans + 'i'

if __name__ == '__main__':
    sol = Solution()
    print(sol.complexNumberMultiply("1+-1i", "1+-1i")) #0+-2i
    print(sol.complexNumberMultiply("1+1i", "1+1i")) #0+2i