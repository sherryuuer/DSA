class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        # 为了不丢失节点联系
        lastNode = self.tail.prev

        newNode.next = self.tail
        newNode.prev = lastNode

        lastNode.next = newNode
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        # save the first node
        firstNode = self.head.next

        newNode.next = firstNode
        newNode.prev = self.head

        firstNode.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        poped = self.tail.prev

        lastNode = self.tail.prev.prev
        lastNode.next = self.tail
        self.tail.prev = lastNode
        return poped.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        poped = self.head.next

        firstNode = self.head.next.next
        firstNode.prev = self.head
        self.head.next = firstNode
        return poped.value
