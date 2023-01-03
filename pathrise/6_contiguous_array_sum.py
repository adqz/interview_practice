# Contiguous sum of array problem

def contiguous_sum(arr, target):
    # TODO: asserts and docstring
    # Brute Force: O(n^3) - Generate all possible sub arrays
    # Time: O(n), Space: O(1). Does sum increase Time?
    # Note: Won't work with negative numbers
    
    i, j = 0, len(arr)
    arr_sum = sum(arr)
    
    while sum(arr[i:j]) != target:
        can_decrease_j = arr_sum - arr[j-1] >= target
        can_increase_i = arr_sum - arr[i] >= target
        # Checking if it is possible to shrink subarray to match target
        if can_decrease_j or can_increase_i:
            if can_decrease_j:
                arr_sum -= arr[j-1]
                j -= 1
            if can_increase_i:
                arr_sum -= arr[i]
                i += 1
        else:
            return False #if cannot decrease either pointers, then we cannot match target
    
    return True

print(contiguous_sum([1,4,6,21], 10)) #True
print(contiguous_sum([1,4,6,0,21], 10)) #True
print(contiguous_sum([1,0,0,0,4,6,0,21], 10)) #True
print(contiguous_sum([1,4,6,21], 9)) #False
print(contiguous_sum([1,4,6,21], 35)) #False