'''
@author: adnan
Problem 3. Longest Substring Without Repeating Characters

Runtime: 784 ms, faster than 7.22% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12 MB, less than 67.97% of Python online submissions for Longest Substring Without Repeating Characters.
'''
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		# 0. Corner case
		if not s:
			return 0
		if len(s) == 1:
			return 1
		
		# 1. General case
		pointer_fixed, pointer_moving = 0, 0
		seen = set()
		longest_str_len = 1
		
		while pointer_moving < len(s):
			# If character is unique
			if s[pointer_moving] not in seen:
				seen.add(s[pointer_moving])
				curr_len = pointer_moving - pointer_fixed + 1 #length of substring
				if curr_len > longest_str_len:
					longest_str_len = curr_len
				pointer_moving += 1 #moving pointer ahead
			else:
				pointer_fixed += 1
				pointer_moving = pointer_fixed
				seen = set()
		
		return longest_str_len

				
if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  print(s.lengthOfLongestSubstring('abc')) #3
  print(s.lengthOfLongestSubstring('abcabcb')) #3
  print(s.lengthOfLongestSubstring('bbbbb')) #1
  print(s.lengthOfLongestSubstring('pwwkew')) #3
  print(s.lengthOfLongestSubstring('abbbccc')) #2
  print(s.lengthOfLongestSubstring('aabcdefa')) #6
  print(s.lengthOfLongestSubstring('')) #0




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