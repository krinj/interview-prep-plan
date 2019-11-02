# Problem: Print the k most frequent numbers in a list.
# Optimal Time: O(n) Space: O(n)

# Example Input: [1, 2, 1, 3, 3, 3], k =2
# Example Output: [3, 1]

def k_most_frequent(arr, k):
    # TODO: Implement me!
    return []

def main():
    arr = [1, 1, 2, 2, 3, 2, 5, 4, 6, 2, 7, 5, 5, 5, 5, 9, 8, 10]
    expected_answer = [5, 2, 1]
    result = k_most_frequent(arr, k=3)
    print(f"Result: {result}")
    if result == expected_answer:
        print("Answer is correct!")
    else:
        print(f"Answer is wrong. Expecting: {expected_answer}")

if __name__ == "__main__":
    main()