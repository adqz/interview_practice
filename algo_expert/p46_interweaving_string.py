def interweavingStrings(one, two, three):
    # Preliminary check
    if len(one) + len(two) != len(three):
        return False
    
    i, j = 0, 0
    for k in range(len(three)):
        if i < len(one) and three[k] == one[i]:
            i += 1
        elif j < len(two) and three[k] == two[j]:
            j += 1
        else:
            return False
    if (i != len(one)) or (j != len(two)):
        return False
    
    return True

if __name__ == "__main__":
    one   = 'aabcc'
    two   = 'dbbca'
    three = 'aadbbcbcac'
    print(interweavingStrings(one, two, three))