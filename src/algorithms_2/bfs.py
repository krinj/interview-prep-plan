# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A 


from collections import deque


def bfs(graph, node, e) -> bool:
    """ Perform Breadth First Search on the graph. Return bool (if element is there). """
    q = deque()
    seen = set()
    seen.add(node)
    q.append(node)

    while len(q) > 0:
        n = q.popleft()
        if n == e:
            return True
        
        for child in graph[n]:
            if child not in seen:
                seen.add(child)
                q.append(child)
        
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
    target = "X"

    result = bfs(graph, root_key, target)
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
