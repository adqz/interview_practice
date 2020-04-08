from collections import deque

# O(n) time | O(w) in space where n = len(arr), w = window_size
def find_max_sliding_window(arr, window_size):
    result = []
    if not arr:
        return result
    if window_size > len(arr):
        return max(arr)
    
    queue = deque([])
    window_start = 0
    for i in range(0, len(arr)):
        # Adjust window start and end
        if i >= window_size:
            window_start += 1
        # Remove indices from the back if they are smaller than current element
        while queue and arr[queue[-1]] <= arr[i]: queue.pop()
        # Remove indices from the front that are greater than start of window
        while queue and window_start > queue[0]: queue.popleft()
        
        queue.append(i)
        if i >= window_size-1:
            result.append(arr[queue[0]])
    
    return result

if __name__ == "__main__":
    print(find_max_sliding_window([-4, 2, -5, 1, -1, 6], window_size=3)) #[2, 2, 1, 6]
