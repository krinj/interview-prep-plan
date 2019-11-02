# Backtracking: N-Queens Problem.
# How many ways can we put N queens on an NxN Chess board where
# none of the queens threaten each other?
# Optimal Time: ?? Space: ??


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}:{self.y}"


def solve(n):
    # n: The number of Queens, and the size of the board.
    # TODO: Implement me!
    count = 1
    return count


def main():
    # For 8 Queens on an 8x8 board, we expect 92 combinations.
    n = 8
    expected_answer = 92

    # Test the algorithm.
    result = solve(n)
    print(f"Result: {result}")
    if result == expected_answer:
        print("Answer is correct!")
    else:
        print(f"Answer is wrong. Expecting {expected_answer}")



if __name__ == "__main__":
    main()