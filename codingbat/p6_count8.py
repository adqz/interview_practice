class Solution:
    '''
    Given a non-negative int n, compute recursively (no loops) the count of the occurrences 
    of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, 
    so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
    while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

    count8(8) → 1
    count8(818) → 2
    count8(8818) → 4
    '''
    def count8(self, num, count=0, prev_was_8 = False):
        # Base case
        if num == 0:
            return count
        # Recursive Case
        digit = num%10
        if digit == 8 and prev_was_8:
            count *= 2
            prev_was_8 = True
        elif digit == 8:
            count += 1
            prev_was_8 = True
        else:
            prev_was_8 = False

        return self.count8(num//10, count, prev_was_8)

if __name__ == "__main__":
    sol = Solution()
    print(sol.count8(1)) #0
    print(sol.count8(123)) #0
    print(sol.count8(8)) #1
    print(sol.count8(818)) #2
    print(sol.count8(8818)) #4
