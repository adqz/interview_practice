'''
@author: adnan
Problem 394. Decode String (Medium)

'''
class Solution:

    # Idea: Treat s like a stack and keep track of '[' and ']' and replicate accordingly

    def decodeString(self, s: str) -> str:
        s = [char for char in s] #converting str to stack/list
        ans = self.helper_decodeString(s, '')
        return ans

    def helper_decodeString(self, s, prev):
        # Base case
        if not s:
            return prev
        
        # General case
        char = s.pop()
        # print(char)
        if char != ']' :
            prev = char + prev
            return self.helper_decodeString(s, prev)
        else:
            str_to_replicate = ''
            while s[-1] != '[':
                char = s.pop()
                if char == ']':
                    # print('Calling again - ', s, prev)
                    return self.helper_decodeString(s, prev)
                str_to_replicate = char + str_to_replicate
            # print(str_to_replicate)
            s.pop() #remove '['
            n = int(s.pop()) #get number of times to replicate
            str_to_replicate *= n
            
            return self.helper_decodeString(s, str_to_replicate + prev)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.decodeString("3[a]2[bc]")) # "aaabcbc"
    print(sol.decodeString("3[a2[c]]")) # "accaccacc"


'''
# Solution 2: Not working. Recursion based. Too many variables to track
class Solution:
    # Idea: Treat s like a stack and keep track of '[' and ']' and replicate accordingly
    def decodeString(self, s: str) -> str:
        s = [char for char in s] #converting str to stack/list
        ans = self.helper_decodeString(s, '', '')
        return ans

    def helper_decodeString(self, s, str_to_replicate, prev, replicate_mode = False):
        # Base case
        if not s:
            return prev
        
        # General case
        char = s.pop()
        # print(char)
        if char.isalpha():
            if replicate_mode:
                return self.helper_decodeString(s, char + str_to_replicate, prev, replicate_mode)
            else:
                return self.helper_decodeString(s, str_to_replicate, char + prev, replicate_mode)
        else:
            if char == ']':
                return self.helper_decodeString(s, str_to_replicate, prev, True)
            if char == '[':
                n = int(s.pop())
                return self.helper_decodeString(s, '', (str_to_replicate + prev)*n, False)
'''


'''
Solution 1: Semi working
class Solution:

    # Idea: Treat s like a stack and keep track of '[' and ']' and replicate accordingly

    def decodeString(self, s: str) -> str:
        s = [char for char in s] #converting str to stack/list
        ans = self.helper_decodeString(s, '')
        return ans

    def helper_decodeString(self, s, prev):
        # Base case
        if not s:
            return prev
        
        # General case
        char = s.pop()
        print(char)
        if char != ']' :
            prev = char + prev
            return self.helper_decodeString(s, prev)
        else:
            str_to_replicate = ''
            while s[-1] != '[':
                char = s.pop()
                if char == ']':
                    print('Calling again - ', s, prev)
                    return self.helper_decodeString(s, prev)
                str_to_replicate = char + str_to_replicate
            # print(str_to_replicate)
            s.pop() #remove '['
            n = int(s.pop()) #get number of times to replicate
            str_to_replicate *= n
            
            return self.helper_decodeString(s, str_to_replicate + prev)
'''

'''
from collections import deque
class Solution:
    # Idea: Go from start to end and keep building string
    def decodeString(self, s: str) -> str:
        s = deque([char for char in s]) #converting str to queue
        ans = self.helper_decodeString(s, '', '')
        
        return ans

    def helper_decodeString(self, s, prev, to_repeat):
        char = s.popleft()
        if char.isdigit():
            num = int(char)
            return num * (self.helper_decodeString(s, prev, to_repeat) + prev)
        if char == '[':
            char = s.popleft()
            while char !=
            temp_str = 
'''