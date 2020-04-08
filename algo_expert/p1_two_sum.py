def twoNumberSum(array, targetSum):
    differences = dict()
    for num in array:
        diff = targetSum - num
        if num in differences:
            return [num, differences[num]]
        else:
            differences[diff] = num
    # print(differences)
    return []

if __name__ == "__main__":
    print(twoNumberSum([4, 6, 1, -3], 3)) #[-3, 6]
    print(twoNumberSum([4, 6, 1, -3], 30)) #[]