def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return merge(left, right)

def merge(left, right):
    arr = []
    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if j >= len(right) or (i < len(left) and left[i] <= right[j]):
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    
    return arr

    


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2, 5]
    result = merge_sort(arr)
    print(result)