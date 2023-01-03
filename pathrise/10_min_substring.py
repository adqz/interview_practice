### ------------------------------------- Min substring problem ------------------------------------- 
from collections import Counter

def get_min_substring(S,T):
    '''
    Time: O(n+m), n = len(S), m = len(T)
    Space: O(m)
    '''
    s, e = 0, 0
    min_substring = ''
    
    while e < len(S):
        if are_characters_in_string(S,T,s,e):
            min_substring = S[s:e]
            s = e
        else:
            e += 1
    
    return min_substring

def are_characters_in_string(S,T,s,e):
    '''
    Time: O((e-s) + m), m = len(T)
    '''
    char_counts = Counter(T)    
    
    for char in S[s:e]:
        if char in char_counts and char_counts[char] > 0:
            char_counts[char] -= 1
    
    if sum(char_counts.values()) == 0:
        return True
    
    return False
    
print(get_min_substring("ADOBECODEBANC", "ABC"))
