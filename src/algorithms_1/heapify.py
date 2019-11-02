def heapify(arr, i, end):
    left = 2 * i + 1
    right = left + 1

    if left >= end:
        return

    v = arr[left]
    idx = left

    if right < end:
        if arr[right] > v:
            v = arr[right]
            idx = right

    if v > arr[i]:
        arr[idx] = arr[i]
        arr[i] = v
        heapify(arr, i, end)

def create_heap(arr):
    m = len(arr) // 2
    for i in range(m, -1, -1):
        heapify(arr, i, len(arr))


def heap_sort(arr):
    create_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        tmp = arr[i]
        arr[i] = arr[0]
        arr[0] = tmp
        heapify(arr, 0, i)

def main():
    arr = [1, 8, 5, 3, 4, 2, 9]
    # create_heap(arr)
    heap_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()