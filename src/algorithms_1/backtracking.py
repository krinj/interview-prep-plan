# N-Queens Problem.
# How many ways can we put N queens on an NxN board?


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}:{self.y}"

def is_safe(q1, q2):
    if q1.x == q2.x or q1.y == q2.y:
        return False

    dx = abs(q1.x - q2.x)
    dy = abs(q1.y - q2.y)

    return dx != dy


def place(board, x, n):
    if x == 0:
        return 1

    count = 0
    for y in range(n):
        q = Queen(x, y)
        safe = True
        for q2 in board:
            if not is_safe(q, q2):
                safe = False
                break

        if safe:
            board.append(q)
            count += place(board, x - 1, n)
            board.pop()
        
    return count


def main():
    n = 8
    result = place([], n, n)
    print(f"Result: {result}")
    pass


if __name__ == "__main__":
    main()