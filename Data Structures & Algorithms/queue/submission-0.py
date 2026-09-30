class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        prev_node = self.tail.prev
        new_node = Node(value, prev_node, self.tail)
        prev_node.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        next_node = self.head.next
        new_node = Node(value, self.head, next_node)
        self.head.next = new_node
        next_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.tail.prev
        val = target.val
        target.prev.next = self.tail
        self.tail.prev = target.prev
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target = self.head.next
        val = target.val
        self.head.next = target.next
        target.next.prev = self.head
        return val
