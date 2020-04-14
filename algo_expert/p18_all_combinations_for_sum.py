# O(2^n) time | O(n) space
def print_all_sum(target):
    output = []  
    result = []
    helper_print_all_sum(target, 0, 1, result, output)
    return output

def helper_print_all_sum(target, curr_sum, start, result, output):
    if curr_sum == target:
        output.append(result[:])
        return
    for i in range(start, target):
        temp_sum = curr_sum + i
        if temp_sum <= target:
            result.append(i)
            helper_print_all_sum(target, temp_sum, i, result, output)
            result.pop() #backtracking
        else:
            return
    
if __name__ == "__main__":
    print(print_all_sum(4))