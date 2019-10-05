# ----------------------- UNSOLVED ----------------------- 314 / 315 test cases passed.
# @author: adnan
# Problem 42. Trapping Rain Water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        assert isinstance(height, list) and len(height) > 0
        assert all( isinstance(el, int) and el>=0 for el in height ), 'Invalid heightuence'

        totalVolume = 0

        for i in range(len(height)):
            currWall = height[i]
            leftCheck = any(currWall < wall for wall in height[:i]) #checkingi if any wall to the left is greater than current walls height
            rightCheck = any(currWall < wall for wall in height[i+1:]) #checkingi if any wall to the right is greater than current walls height
            canHoldWater = leftCheck and rightCheck #current wall can hold water if there are walls on either side greater in height
            # print('leftCheck, rightCheck, canHoldWater = ', leftCheck, rightCheck, canHoldWater)
            if canHoldWater:
                maxHeightLeft = max(height[:i])
                maxHeightRight = max(height[i+1:])

                for rightWall in height[i+1:]:
                    if rightWall >= maxHeightLeft:
                        maxHeightRight = rightWall
                        break;

                currVolume = min(maxHeightRight, maxHeightLeft) - currWall
                # print('maxHeightLeft, maxHeightRight, currWall, currVolume = ', maxHeightLeft, maxHeightRight, currWall, currVolume)
                totalVolume += currVolume
        print(totalVolume)
        return totalVolume

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  seq1 = [2, 1, 2]
  seq2 = [3, 0, 1, 3, 0, 5]
  seq3 = [6, 7, 8, 0, 4, 6, 8, 0, 3, 5, 5, 6, 3, 0, 9]
  seq4 = [1,2,1,3]
  seq5 = [2, 1]
  seq6 = [0,1,0,2,1,0,1,3,2,1,2,1]
  assert s.trap(seq1) == 1, 'Total volume should be 1'
  assert s.trap(seq2) == 8, 'Total volume should be 8'
  assert s.trap(seq3) == 48, 'Total volume should be 48'
  assert s.trap(seq4) == 1, 'Total volume should be 1'
  assert s.trap(seq5) == 0, 'Total volume should be 0'
  assert s.trap(seq6) == 6, 'Total volume should be 6'
  print('All test cases passed!')