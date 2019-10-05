# ----------------------- UNSOLVED ----------------------- 986 / 987 test cases passed
# @author: adnan
# Problem 3. Longest Substring Without Repeating Characters
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# assert isinstance(s, str) and len(s) >= 0
		# return 0 if s == ''
		if s=='':
			return 0
		oldSubstring = ''
		longestSubstring = s[0]
		i = 0
		while (i != len(s)-1):
			# print(i)
			newSubstring = ''
			for j in range(i, len(s)):
				if (s[j] in newSubstring):
					break
				else:
					newSubstring += s[j]
					# print(newSubstring)
			if len(newSubstring) > len(oldSubstring):
				longestSubstring = newSubstring
				oldSubstring = newSubstring
			i = j

		return len(longestSubstring)

if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  print(s.lengthOfLongestSubstring('abc'))
  print(s.lengthOfLongestSubstring('abca'))
  print(s.lengthOfLongestSubstring('abbbccc'))
  print(s.lengthOfLongestSubstring('aabcdefa'))
  print(s.lengthOfLongestSubstring(''))




  '''
  Solution 1:

  class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# assert isinstance(s, str) and len(s) >= 0
		if s == '':
			return 0
		oldSubstring = ''
		longestSubstring = s[0]

		for i in range(0, len(s)):
			# print(i)
			newSubstring = ''
			for j in range(i, len(s)):
				if (s[j] in newSubstring):
					break
				else:
					newSubstring += s[j]
					# print(newSubstring)
			if len(newSubstring) > len(oldSubstring):
				longestSubstring = newSubstring
				oldSubstring = newSubstring

		return len(longestSubstring)

  '''