# O(n) time | O(n) space
def remove_duplicates(string):
    seen = set()
    i = 0 
    while i < len(string):
        if string[i] in seen:
            string = string[:i] + string[i+1:]
        else:
            seen.add(string[i])
            i += 1
    # print(string)
    return string

if __name__ == "__main__":
    print(remove_duplicates('aabbcaacbcacbccc'))
    print(remove_duplicates(''))
    print(remove_duplicates('aaaaa'))

'''
## Given solution that doesn't work because strings are immutable in python!!
def remove_duplicates(string):
    seen = set()
    read_index, write_index = 0, 0

    while read_index < len(string):
        if string[read_index] not in seen:
            seen.add(string[read_index])
            string[write_index] = string[read_index]
            read_index  += 1
            write_index += 1
        else:
            read_index += 1
    
    string = string[:write_index]
    return
'''