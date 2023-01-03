'''

Given a positive int n, print all jumping numbers smaller than or equal to n. A number is called a jumping number if all adjacent digits in it differ by 1. 
For example, 8987 and 4343456 are jumping numbers, but 796 and 89098 are not. All single digit numbers are considered as jumping numbers.

Example:
Input: 105
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101]
'''

class Solution:
    '''
    Time: O(2^N) N is the depth of the tree
    Space: O(# of jumping numbers)
    '''
    def __init__(self):
        self.ans = []

    def get_jumping_numbers(self, n):
        # TODO: asserts and docstring
        if n <= 10:
            jumping_numbers_less_than_10 = list(range(0,n+1))
            return jumping_numbers_less_than_10
        else:
            jumping_numbers_less_than_10 = list(range(0,11))

        jumping_numbers_greater_than_10 = self.generate_jumping_numbers(n)
        
        return jumping_numbers_less_than_10 + jumping_numbers_greater_than_10

    def generate_jumping_numbers(self, max_number):
        number_of_digits = len(str(max_number))
        
        for depth in range(2, number_of_digits+1):
            for root_node in range(1, 10):
                self.generate_jumping_numbers_for_n_digits(root_node, 1, depth, max_number, root_node)
        
        return self.ans

    def generate_jumping_numbers_for_n_digits(self, curr_node, curr_depth, max_depth, max_number, curr_number):
        # Base
        if curr_depth == max_depth and curr_number <= max_number:
            self.ans.append(curr_number)
            return

        # Build
        curr_digit = curr_number % 10
        for move in [-1, +1]:
            next_digit = curr_digit + move
            if 0 <= next_digit <= 9:
                next_number = curr_number*10 + next_digit
                if next_number <= max_number:
                    self.generate_jumping_numbers_for_n_digits(next_digit, curr_depth+1, max_depth, max_number, next_number)
                    
    
if __name__ == "__main__":
    sol = Solution()
    ans = sol.get_jumping_numbers(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(ans)
    ans = sol.get_jumping_numbers(50) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45]
    print(ans)
    ans = sol.get_jumping_numbers(105) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98, 101]
    print(ans)

'''
Rough work
----------

1 digit = 10   | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
2 digit = 17   | 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98
                  D   U
3 digit =      | 

101, 123, 121
210, 212, 232, 234
321, 323, 345, 343
3DD, 3DU, 3UU, 3UD

5432, 5434,  54343
5DDD, 5DDDU, 5DDUD,

Brute force:
iterate from all nums from 1 to N
 if < 10 
   just 0-10
 else
   checkIfJumpingNumber(num) // O(num_of_digits)

O(N*d) LINEAR? Factorial? Exponential?

3 digit

               1                          2                         3 ... 9
                  
           0      2                  1         3
                 / \
                1   3
             
'''