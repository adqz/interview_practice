# O(logn) time | O(logn) space
def integer_divide(dividend, divisor):
    ''' Only for positive integers '''
    # Four corner cases
    if divisor == 0:
        return -1
    if divisor == 1:
        return dividend
    if dividend < divisor:
        return 0
    if dividend == divisor:
        return 1
    
    quotient = 1
    temp = divisor

    # Keep doubling quotient and temp until temp >= dividend
    while temp < dividend:
        quotient <<= 1
        temp <<= 1
    
    # Left shiting (or dividing by 2) if temp > dividend
    if temp > dividend:
        temp >>=1
        quotient >>=1
    
    return quotient + integer_divide(dividend-temp, divisor)

if __name__ == "__main__":
    print(integer_divide(7,0)) #-1
    print(integer_divide(13,1)) #13
    print(integer_divide(57,57)) #1
    print(integer_divide(8,4)) #2
    print(integer_divide(40, 8)) #5