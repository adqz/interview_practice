def interweavingStrings(one, two, three):
    # Preliminary check
    if len(one) + len(two) != len(three):
        return False

    return helper_interweavingStrings(one, two, three, 0, 0)
    
def helper_interweavingStrings(one, two, three, i, j):
    k = i+j
    # Base case
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
        if helper_interweavingStrings(one, two, three, i+1, j):
            return True
    
    if j < len(two) and two[j] == three[k]:
        if helper_interweavingStrings(one, two, three, i, j+1):
            return True

    return False

if __name__ == "__main__":
    one   = 'aabcc'
    two   = 'dbbca'
    three = 'aadbbcbcac'
    print(interweavingStrings(one, two, three))