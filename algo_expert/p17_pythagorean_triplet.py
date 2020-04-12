# O(n^2) time | O(logn) space
def find_pythagorean_triplets(arr):
    triplets = []
    arr.sort() #inplace sorting
    for i in range(len(arr)):
        if arr[i] == 0: continue
        c2 = arr[i]**2

        start, end = 0, len(arr)-1
        while start < end:
            if start == i or arr[start] == 0:
                start += 1
                continue
            if end == i or arr[end] == 0:
                end -= 1
                continue
            a2 = arr[start]**2
            b2 = arr[end]**2
            sum = a2 + b2 - c2

            if sum == 0:
                triplets.append((arr[start], arr[i], arr[end]))
                break
            elif sum > 0:
                end -= 1
            else:
                start += 1
            
    return triplets

if __name__ == "__main__":
    print(find_pythagorean_triplets([0])) #[]
    print(find_pythagorean_triplets([4,6,10,5,7,25])) #[]
    print(find_pythagorean_triplets([4,6,10,5,8,25])) #[6,8,10]