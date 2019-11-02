class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, x):
        n = Node(x)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.size += 1
    
    def pop(self):
        x = self.head.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1
        return x

    def traverse(self):
        node = self.head
        s = []
        while node is not None:
            s.append(node.val)
            node = node.next
        
        print(" -> ".join(map(str, s)))

if __name__ == "__main__":
    linked = LinkedList()

    linked.add(6)
    linked.add(7)
    linked.add(8)
    linked.add(2)
    linked.add(15)

    linked.pop()
    linked.pop()
    linked.pop()

    linked.add(1)
    linked.add(3)

    linked.traverse()
