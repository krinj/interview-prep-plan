def visualize_tree(node):
    layers = []
    depth = max_depth(node, 0)
    add_to_layer(node, 0, layers, depth)
    layers = layers[:-1]  # Delete the last null layer.

    n_last_elements = len(layers[-1])
    full_length = n_last_elements * 2 - 1
    segment_length = full_length
    mid_points = [full_length // 2]

    for i, layer in enumerate(layers):

        line = [" "] * full_length
        connector = [" "] * full_length

        new_mid_points = []

        segment_length //= 2

        for j, n in enumerate(layer):

            m = mid_points[j]
            left = m - segment_length // 2 - 1
            right = m + segment_length // 2 + 1
            new_mid_points.append(left)
            new_mid_points.append(right)

            if n is None:
                line[m] = "•"
            else:
                line[m] = str(n)

            if i < len(layers) - 1: 
                
                for l in range(left, right):
                    connector[l] = "─"

                connector[m] = "┴"
                connector[left] = "┌"
                connector[right] = "┐"

        mid_points = new_mid_points
        line_str = "".join(line)
        conn_str = "".join(connector)
        print(line_str)
        if i < len(layers) - 1:
            print(conn_str)

def max_depth(node, d):
    if node is None:
        return d
    else:
        d += 1
        d1 = max_depth(node.left, d)
        d2 = max_depth(node.right, d)
        return max(d1, d2)

def add_to_layer(node, d, layers, max_d):
    while len(layers) <= d:
        layers.append([])
    
    layers[d].append(node)
    if node is None:
        if d < max_d:
            add_to_layer(None, d + 1, layers, max_d)
            add_to_layer(None, d + 1, layers, max_d)
    else:
        add_to_layer(node.left, d + 1, layers, max_d)
        add_to_layer(node.right, d + 1, layers, max_d)


class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.val)

if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    D.left = G

    visualize_tree(A)