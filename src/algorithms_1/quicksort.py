# Optimal Time: O(nlogn) Space: O(n)

def quicksort(arr, low, high):
    # Sort an array in place, between index low, and index high.
    return arr
    

def test_quicksort(arr):
    return quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    expected_result = sorted(arr)

    test_quicksort(arr)
    print(f"Result: {arr}")

    if str(expected_result) == str(arr):
        print("Answer is correct!")
    else:
        print(f"Answer is wrong. Got: {arr} Expected: {expected_result}")