def partition(arr, low, high):
    i = low
    j = i + 1

    while j < high:
        if arr[j] < arr[i]:
            tmp = arr[i]
            arr[i] = arr[j]
            if j == i + 1:
                arr[j] = tmp
            else:
                arr[j] = arr[i + 1]
                arr[i + 1] = tmp
            i += 1
        j += 1
                
    return i
    

def quicksort(arr, low, high):
    if high - low <= 1:
        return
    
    i = partition(arr, low, high)
    quicksort(arr, low, i)
    quicksort(arr, i + 1, high)
    

def test_quicksort(arr):
    return quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    result = test_quicksort(arr)
    print(arr)