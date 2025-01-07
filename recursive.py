def find_min_max_recursive(arr, start, end):
    if start == end:
        return arr[start], arr[start]
    
    mid = (start + end) // 2
    left_min, left_max = find_min_max_recursive(arr, start, mid)
    right_min, right_max = find_min_max_recursive(arr, mid + 1, end)
    
    return min(left_min, right_min), max(left_max, right_max)