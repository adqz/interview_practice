'''
@author: adnan
Problem 38. Count and Say (Easy)

Runtime: 32 ms, faster than 73.70% of Python3 online submissions for Count and Say.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Count and Say.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.helper_countAndSay('1', 1, n)
    def helper_countAndSay(self, num_to_say, curr_n, target_n):
        # Base Case
        if curr_n == target_n:
            return num_to_say
        
        curr_char_to_count = num_to_say[0]
        freq = 0
        next_num_to_say = ''
        for num in num_to_say+'X': #adding extra X as a dummy so we can count the last element
            if num == curr_char_to_count:
                freq += 1
            else:
                next_num_to_say += str(freq) + str(curr_char_to_count)
                curr_char_to_count = num
                freq = 1
        return self.helper_countAndSay(next_num_to_say, curr_n + 1, target_n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1)) # '1'
    print(sol.countAndSay(2)) # '11'
    print(sol.countAndSay(3)) # '21'
    print(sol.countAndSay(4)) # '1211'
    print(sol.countAndSay(5)) # '111221'
    