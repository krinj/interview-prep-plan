# Binary search:
# Input is an array of sorted integers, and an integer, k.
# Output: Index of k if it exists in the array, else -1.


def binary_search(arr, x, low, high):
    delta = high - low
    if delta == 0:
        return -1

    i = low + delta // 2

    if arr[i] == x:
        return i
    
    if arr[i] > x:
        return binary_search(arr, x, low, i)
    else:
        return binary_search(arr, x, i + 1, high)


def test_binary_search(arr, search_func):
    for i, n in enumerate(arr):
        result = search_func(arr, n, 0, len(arr))
        if result != i:
            return f"FAILURE: {n} was found at index {result}. Expected: {i}"
    return "SUCCESS"


if __name__ == "__main__":
    arr = [-2, -1, 0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 100]
    result = test_binary_search(arr, binary_search)
    print(result)
    print(binary_search(arr, 99, 0, len(arr)))
