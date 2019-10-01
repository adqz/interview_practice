# @author: adnan
# Problem 13. Roman to Integer
class Solution(object):
	def __init__(self):
		self.r2i = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
		}
	def romanToInt(self, s):
		"""
		Given a roman numeral, convert it to an integer. 
		Input is guaranteed to be within the range from 1 to 3999

		:type s: str
		:rtype: int
		"""
		# assert isinstance (s, str) and len(s) >= 0
		s = list(s)
		intNumber = 0
		lastRoman = ''
		while (s):
			currRoman = s.pop()
			if (currRoman == 'I' and (lastRoman == 'V' or lastRoman == 'X')):
				intNumber -= 1
				continue
			if (currRoman == 'X' and (lastRoman == 'C' or lastRoman == 'L')):
				intNumber -= 10
				continue
			if (currRoman == 'C' and (lastRoman == 'D' or lastRoman == 'M')):
				intNumber -= 100
				continue
			intNumber += self.r2i[currRoman]
			lastRoman = currRoman

		return intNumber

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  print(s.romanToInt('III'))
  print(s.romanToInt('XLIV'))
  print(s.romanToInt('LVIII'))
  print(s.romanToInt("MCMXCIV"))
  












		