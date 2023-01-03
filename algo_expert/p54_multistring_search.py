def multiStringSearch(bigString, smallStrings):
    word_lookup = set(bigString.split(' '))
    result = []
    for word in smallStrings:
        if word in word_lookup:
            result.append(True)
        else:
            for word_match in
    
    return result