def interweavingStrings(one, two, three):
    # Preliminary check
    if len(one) + len(two) != len(three):
        return False
    
    # Build count dictionary
    character_count = dict()
    for char in one:
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1
    for char in two:
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1
    
    for char in three:
        if char not in character_count:
            return False
        character_count[char] -= 1
    
    for char, count in character_count.items():
        if count != 0:
            return False
    
    return True