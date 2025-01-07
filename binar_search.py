def find_min_max_binary(arr):
    arr.sort()  # Urutkan array
    return arr[0], arr[-1]