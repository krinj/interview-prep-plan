

def knapsack(arr, i, w, memo):
    if i < 0:
        return 0, []

    key = (i, w)
    if key in memo:
        return memo[key]

    v, sack = knapsack(arr, i - 1, w, memo)
    item = arr[i]
    if item.weight <= w:
        v2, sack2 = knapsack(arr, i - 1, w - item.weight, memo)
        v2 += item.value
        if v2 > v:
            v = v2
            sack = sack2[:]
            sack.append(item.key)
    
    memo[key] = v, sack
    return memo[key]


class Item:
    def __init__(self, k, v=10, w=10):
        self.key = k
        self.value = v
        self.weight = w


def main():
    items = [
        Item("A", 120, 30),
        Item("B", 70, 20),
        Item("C", 500, 5),
        Item("D", 100, 15),
        Item("E", 15, 1),
        Item("F", 200, 80)
    ]
    max_weight = 50
    memo = {}
    result = knapsack(items, len(items) - 1, max_weight, memo)
    print(f"Results: {result}")


if __name__ == "__main__":
    main()