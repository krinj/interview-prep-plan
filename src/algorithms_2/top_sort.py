# A 🡪 B 🡪 C
# 🡫       
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I  


def top_sort(graph):
    d_count = {k: 0 for k in graph}
    for _, children in graph.items():
        for c in children:
            d_count[c] += 1
    q = [k for k, v in d_count.items() if v == 0]
    result = []
    while len(q) > 0:
        n = q.pop()
        result.append(n)
        for c in graph[n]:
            d_count[c] -= 1
            if d_count[c] == 0:
                q.append(c)
    if len(result) == len(graph):
        return result
    return None


def make_graph():
    graph = {
        "A": ["B", "E"],
        "B": ["C", "D"],
        "C": [],
        "D": ["F"],
        "E": ["D", "G"],
        "F": ["I"],
        "G": ["H"],
        "H": ["I"],
        "I": []
    }
    return graph


def main():
    graph = make_graph()
    result = top_sort(graph)
    print(f"Topological Sort: {result}")


if __name__ == "__main__":
    main()