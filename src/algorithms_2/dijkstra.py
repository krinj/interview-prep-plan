# A ── B ── C
# │    │    
# E ── D ── F
# │         │
# G ── H ── I  

import sys
import heapq

def dijkstra(graph, start, end):
    paths = {k: (sys.maxsize, None) for k in graph}
    paths[start] = (0, None)
    q = [(0, start)]

    while len(q) > 0:
        d, n = heapq.heappop(q)
        if n == end:
            result = []
            while n != start:
                result.append(n)
                n = paths[n][1]
            result.append(n)
            result.reverse()
            return d, result
        
        for c, w in graph[n].items():
            d2 = d + w
            if d2 < paths[c][0]:
                paths[c] = (d2, n)
                heapq.heappush(q, (d2, c))

    return -1, []

def make_graph():
    graph = {
        "A": {"B": 3, "E": 2},
        "B": {"C": 1, "D": 1, "A": 1},
        "C": {"B": 1},
        "D": {"B": 6, "E": 1, "F": 1},
        "E": {"A": 1, "D": 5, "G": 1},
        "F": {"D": 1, "I": 1},
        "G": {"E": 10, "H": 1},
        "H": {"G": 1, "I": 3},
        "I": {"H": 1, "F": 2}
    }
    return graph


def main():
    graph = make_graph()
    origin = "I"
    target = "A"
    cost, path = dijkstra(graph, origin, target)
    print(f"Path from {origin} to {target}: {path} | Cost: {cost}")


if __name__ == "__main__":
    main()