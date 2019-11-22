'''
@author: adnan
Problem No. 11 (Medium)
Runtime: 108 ms, faster than 51.35% of Python online submissions for Container With Most Water.
Memory Usage: 13.1 MB, less than 30.51% of Python online submissions for Container With Most Water.
'''
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) in [0,1]:
      return 0
    if len(height) == 2:
      return min(height[1],height[0])
    
    p1, p2 = 0, len(height)-1
    vol = []
    while abs(p2-p1) != 0:
      area = min(height[p1], height[p2]) * (p2-p1)
      vol.append(area)
      if height[p2] < height[p1]:
        p2 -= 1
      else:
        p1 += 1
    return max(vol)

if __name__ == '__main__':

  s = Solution()
  testcase = [3,1,2,1]
  ans = s.maxArea(testcase)
  print(f'ans = {ans}')
  testcase = [1,8,6,2,5,4,8,3,7]
  ans = s.maxArea(testcase)
  print(f'ans = {ans}')
  testcase = [1,0]
  ans = s.maxArea(testcase)
  print(f'ans = {ans}')


'''
# O(n2)
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    vol = []
    for i in range(len(height)-1):
      for j in range(i+1, len(height)):
        vol.append(min(height[i], height[j]) * (j-i))
    return max(vol)
'''