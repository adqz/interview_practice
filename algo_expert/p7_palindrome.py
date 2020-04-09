# O(logn) time | O(1) Space
def isPalindrome(string):
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    print(isPalindrome('adnan')) #False
    print(isPalindrome('madam')) #True