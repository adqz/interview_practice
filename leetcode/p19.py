class Solution(object):
  def sortArrayByParity(self, A):
    even = 0
    odd = len(A)-1
    while(even != odd):
      if (A[even]%2==0):
        even += 1
      else:
        A[even], A[odd] = A[odd], A[even]
        odd -= 1
    return A

if __name__ == '__main__':
  s = Solution()
  A = [3, 1, 2, 4]
  print(s.sortArrayByParity(A))

'''
class Solution(object):
  def isEven(self, num):
    return (num%2 == 0)
  def isOdd(self, num):
    return not(self.isEven(num))
  def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even = 0
    odd = len(A)-1
    while(even <= odd):
      if (self.isEven(A[even])):
        even += 1
      else:
        A[even], A[odd] = A[odd], A[even]
        odd -= 1
    return A
'''