class Solution(object):
  def sortArrayByParityII(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    i, odd, even = 0, 1, 0
    while(i < len(A) or even < len(A) or odd < len(A)):
      print(A, i, even, odd)
      try:
        if(A[i] % 2==0 and i%2==0):
          i = i+1
          # even+=2
          continue
        if(A[i] % 2!=0 and i%2!=0):
          i = i+1
          # odd+=2
          continue
        if (A[i]%2==0 and i%2!=0):
          A[i], A[even] = A[even], A[i]
          even += 2
          continue
        if (A[i]%2!=0 and i%2==0):
          A[i], A[odd] = A[odd], A[i]
          odd += 2
          continue
      except IndexError:
        return A
    return A

if __name__ == '__main__':
  s = Solution()
  A = [4, 2, 5, 7]
  A = [3,1,4,2]
  A = [4,1,1,0,1,0]
  # A = [3, 4]
  print(s.sortArrayByParityII(A))