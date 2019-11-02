# Problem: Print the k most frequent numbers in a list.

def k_most_frequent(arr, k):
    f_map = {}
    for x in arr:
        if x in f_map:
            f_map[x] += 1
        else:
            f_map[x] = 1
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for x, count in f_map.items():
        buckets[count].append(x)
    result = []
    for i in range(n - 1, -1, -1):
        b = buckets[i]
        for x in b:
            result.append(x)
            if len(result) == k:
                return result
    return None

def main():
    arr = [1, 1, 2, 2, 3, 2, 5, 4, 6, 2, 7, 5, 5, 5, 5, 9, 8, 10]
    print(k_most_frequent(arr, k=3))

if __name__ == "__main__":
    main()