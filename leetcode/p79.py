'''
@author: adnan
Problem 686. Repeated String Match

'''
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # 0. Corner case
        if not A or not B:
            return -1
        # 1. Find start point of B in A
        j, num_repeat = 0, 0
        for i in range(len(A)):
            if A[i] == B[j]:
                if i == 0:
                    break
                else:
                    num_repeat = 1
                    break
        # 2. Matching A in B and counting number of times its needed
        while j<len(B):
            # Increasing pointers at A and B
            if B[j] == A[i]:
                # Increase num_repeat if we need first character of A again
                if i == 0:
                    num_repeat += 1
                if i == len(A) - 1:
                    i = 0
                    j += 1
                else:
                    i += 1
                    j += 1
            else:
                return -1
        
        return num_repeat

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedStringMatch(A = "abcd", B = "cdabcdab")) #3
    print(sol.repeatedStringMatch(A = "abcd", B = "abcdabcd")) #3
    print(sol.repeatedStringMatch(A = "aac", B = "aaac")) #3