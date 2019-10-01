# ----------------------- UNSOLVED ----------------------- 8 / 1158 test cases passed
# @author: adnan
# Problem 6. ZigZag Conversion
import numpy as np
class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		masterArr = []
		for i in range(0, numRows):
			masterArr.append([])
		print(masterArr)

		lineIndex = 0
		sign = 1
		for char in s:
			# print(lineIndex)
			masterArr[lineIndex].append(char)
			if (lineIndex == numRows-1):
				sign = -1
			if(lineIndex == 0):
				sign = 1
			lineIndex += sign*1

		ans = ''
		for i in range(0, numRows):
			ans += ''.join(masterArr[i])
		# print(ans)
		return ans

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  # s.convert('abcdefghijkl', 4)
  # s.convert('PAYPALISHIRING', 4)
  s.convert('AB', 1)