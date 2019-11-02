from vis_tree import visualize_tree

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
    
    def get_height(self):
        left_height = -1 if self.left is None else self.left.get_height()
        right_height = -1 if self.right is None else self.right.get_height()
        return max(left_height, right_height) + 1

    def add(self, n):
        if n.val > self.val:
            if self.right == None:
                self.right = n
                n.parent = self
            else:
                self.right.add(n)
        else:
            if self.left == None:
                self.left = n
                n.parent = self
            else:
                self.left.add(n)

    def __repr__(self):
        return f"{self.val}"


class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, x):
        n = Node(x)
        if self.root is None:
            self.root = n
        else:
            self.root.add(n)
        self.balance(n)

    def balance(self, n):

        if not self.is_balanced(n):
            print(f"Rebalance: {n}")
            visualize_tree(n)

            r_size = self.get_height(n.right)
            l_size = self.get_height(n.left)

            if r_size > l_size:
                c = n.right
                rc_size = self.get_height(c.right)
                lc_size = self.get_height(c.left)

                if rc_size > lc_size:
                    print("LEFT ROTATION")
                    self.rotate_left(n)
                else:
                    print("R L")
                    self.rotate_right(c)
                    self.rotate_left(n)
            else:
                c = n.left
                rc_size = self.get_height(c.right)
                lc_size = self.get_height(c.left)

                if lc_size > rc_size:
                    print("R")
                    self.rotate_right(n)
                else:
                    print("L R")
                    self.rotate_left(c)
                    self.rotate_right(n)
            # Figure out how it is imbalanced...
            # Try to balance it.
            # Recurse upwards to the root.
            print("After Rotation")
            visualize_tree(n.parent)

        if n.parent is None:
            self.root = n
            return
        else:
            self.balance(n.parent)

    def get_height(self, n):
        if n is None:
            return -1
        else:
            return n.get_height()

    def is_balanced(self, n):
        left_size = self.get_height(n.left)
        right_size = self.get_height(n.right)
        delta = abs(left_size - right_size)
        return delta <= 1

    def rotate_left(self, n):
        x = n.right

        # Swap 1
        n.right = x.left
        if x.left is not None:
            x.left.parent = n

        # Swap 2
        p = n.parent
        if p is not None:
            if p.left == n:
                p.left = x
            else:
                p.right = x
        x.parent = n.parent

        # Swap 3
        x.left = n
        n.parent = x

    def rotate_right(self, n):
        x = n.left

        # Swap 1
        n.left = x.right
        if x.right is not None:
            x.right.parent = n

        # Swap 2
        p = n.parent
        if p is not None:
            if p.left == n:
                p.left = x
            else:
                p.right = x
        x.parent = n.parent

        # Swap 3
        x.right = n
        n.parent = x


def traverse(n):
    if n is None:
        return

    traverse(n.left)
    print(n)
    traverse(n.right)

def main():
    arr = [4, 7, 10, 12, 40, 21, 2, 1, 5, 6, 8, 9, 3]
    tree = AVLTree()
    for x in arr:
        tree.add(x)

    print("Final Tree")
    visualize_tree(tree.root)
    traverse(tree.root)
    pass

if __name__ == "__main__":
    main()