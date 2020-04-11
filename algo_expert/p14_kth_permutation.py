def find_kth_permutation(arr, k, result=[]):
    if len(arr) == 0:
        return ''.join(result)
    
    n = len(arr)
    block_size = factorial(n-1)
    block_index = (k-1) // block_size
    k -= (block_size*block_index)
    selected_number = str(arr.pop(block_index))
    result.append(selected_number)
    
    return find_kth_permutation(arr, k, result)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print(find_kth_permutation([], 8, [])) #
    print(find_kth_permutation([1,2,3,4], 8, [])) #2143
    print(find_kth_permutation([1,2,3], 3, [])) #213
