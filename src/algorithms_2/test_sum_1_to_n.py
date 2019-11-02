
def sum_1_to_n(n):
    return ((n + 1) * n) // 2


def test_sum_1_to_n(n, func):
    expected = sum([x + 1 for x in range(n)])
    output = func(n)
    if output == expected:
        print(f"Success: {output} (expected {expected})")
    else:
        print(f"Failed: {output} (expected {expected})")


if __name__ == "__main__":
    test_sum_1_to_n(100, sum_1_to_n)
    test_sum_1_to_n(5, sum_1_to_n)
    test_sum_1_to_n(1, sum_1_to_n)
    test_sum_1_to_n(90, sum_1_to_n)