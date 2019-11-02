# Merge Sort: O(nlogn) sorting algorithm.

def merge_sort(arr):
    return arr

def merge(left, right):
    return left + right

    
if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2, 5]
    expected_answer = sorted(arr)
    result = merge_sort(arr)

    print(f"Result: {result}")
    if expected_answer == result:
        print("Answer is correct!")
    else:
        print(f"Answer is wrong. Expected: {expected_answer}")
    