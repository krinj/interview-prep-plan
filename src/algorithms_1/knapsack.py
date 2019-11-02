
def knapsack(arr, capacity):
    # Given an array of items (each with weight and value), find the max
    # value of items that can be fit into a bag with weight capacity. 
    # Return: value of the items, and a list of the items that should be in the bag.
    
    # TODO: Implement me!
    
    value = 0
    items = []
    return value, items


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
    capacity = 50
    expected_value = 720
    expected_items = ["A", "C", "D"]
    
    value, items = knapsack(items, capacity)
    print(f"Results: {value}, {items}")

    if expected_value != value:
        print(f"Wrong value. Got {value}. Expected {expected_value}.")

    if expected_items != items:
        print(f"Wrong items. Got {items}. Expected {expected_items}.")
    
    if (expected_items == items) and (expected_value == value):
        print("Answer is correct!")


if __name__ == "__main__":
    main()