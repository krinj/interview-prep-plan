class Node:
    def __init__(self, v=None):
        self.k = None
        self.v = v
        self.next = None

    def __repr__(self):
        return f"{self.k}: {self.v}"

    def __str__(self):
        return self.__repr__()


class HashMap:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.resize(4)

    def resize(self, new_size):
        new_arr = [Node() for _ in range(new_size)]
        for n in self.arr:
            while n.k is not None:
                self.insert(new_arr, n.k, n.v)
                n = n.next
        self.arr = new_arr

    def index(self, k, cap):
        return hash(k) % cap        

    def insert(self, arr, k, v):
        i = self.index(k, len(arr))
        n = arr[i]
        while True:
            if n.k is None:
                n.next = Node()
                n.k = k
                break
            if n.k == k:
                break
            n = n.next
        n.v = v 

    def add(self, k, v):
        if self.size >= len(self.arr):
            self.resize(len(self.arr) * 2)
        self.insert(self.arr, k, v)
        self.size += 1

    def get(self, k):
        i = self.index(k, len(self.arr))
        n = self.arr[i]
        while n.k is not None:
            if n.k == k:
                return n.v
            n = n.next
        return None

    def describe(self):
        for i, sub in enumerate(self.arr):
            n = sub
            line = []
            while n.k is not None:
                line.append(str(n))
                n = n.next
            line_str = " -> ".join(line)
            print(f"{i}: {line_str}")
    
def main():
    h = HashMap()
    h.add("A", 5)
    h.add("B", 3)
    h.add("C", 8)
    h.add("D", 8)
    h.add("E", 8)
    h.add("F", 8)
    h.add("A", 2)
    h.describe()

    print(h.get("A"))
    print(h.get("B"))
    print(h.get("C"))
    print(h.get("X"))


if __name__ == "__main__":
    main()