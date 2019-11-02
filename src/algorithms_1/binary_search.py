# Binary search:
# Input is an array of sorted integers, and an integer, k.
# Output: Index of k if it exists in the array, else -1.


def binary_search(arr, x):
    """
    Given: 
        arr: a sorted list of numbers.
        x: a target number.
    Return the index of x in the array (if it exists) or -1 if it doesn't.
    """
    # TODO: Implement me!

    return -1


def test_binary_search(arr, search_func):
    for i, n in enumerate(arr):
        result = search_func(arr, n)
        if result != i:
            return f"FAILURE: {n} was found at index {result}. Expected: {i}"
    return "SUCCESS"


if __name__ == "__main__":
    arr = [-2, -1, 0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 100]
    result = test_binary_search(arr, binary_search)
    print(result)
