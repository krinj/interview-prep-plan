# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A... 


from collections import deque


def dfs(graph, node, x) -> bool:
    """ Perform Depth First Search on the graph. Return bool (if element is there). """
    stack = [node]
    seen = set()
    seen.add(node)

    while len(stack) > 0:
        n = stack.pop()
        if n == x:
            return True
        for c in graph[n]:
            if c not in seen:
                seen.add(c)
                stack.append(c)
    
    return False


def generate_graph():
    graph = {
        "A": ["B", "E"],
        "B": ["C", "D"],
        "C": [],
        "D": ["F"],
        "E": ["D", "G"],
        "F": ["I"],
        "G": ["H"],
        "H": ["I"],
        "I": ["A"]
    }
    return graph


def main():
    graph = generate_graph()

    root_key = "A"
    target = "I"

    result = dfs(graph, root_key, target)
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
