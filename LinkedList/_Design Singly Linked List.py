class Node:

    def __init__(self, val, next_node=None):
        """为什么要定义next
        面向对象就是要给对象赋予所有的功能
        此处有pointer的功能当然要定义"""
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        # 不要加length了，需要再加
        self.head = None
        self.tail = self.head

    def get(self, index: int) -> int:
        # loop的时候用指针检索是否有下一个
        cur = self.head
        i = 0
        # if index == 0:
        #     return -1
        # ^is a set,i = 0 and cur is there
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
            # ^the set moves
        return -1  # index out

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        if not node.next:  # if the node is the only node, it is alse the tail
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        # head situation
        if index == 0:
            if self.head:
                if self.head.next:
                    self.head = self.head.next
                    return True
                else:
                    self.head = None
                    self.tail = None
                    return True
            else:
                return False

        cur = self.head
        i = 0
        while cur.next:
            # if next node exists and hit the index
            # 这是我自己理解的方式，我觉得自己理解了比照搬别人的code好很多
            if i + 1 == index:

                if cur.next == self.tail:
                    self.tail = cur

                cur.next = cur.next.next
                return True
            cur = cur.next
            i += 1

        return False

    def getValues(self):
        cur = self.head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr


# Example usage:
my_linked_list = LinkedList()
# print(my_linked_list.getValues())

# my_linked_list.insertHead(1)
# print(my_linked_list.getValues())

my_linked_list.insertTail(1)
# print(my_linked_list.getValues())

my_linked_list.insertTail(2)
# print(my_linked_list.getValues())  # Output: [1, 2, 3]

print(my_linked_list.get(1))  # 2

# my_linked_list.remove(1)
# print(my_linked_list.getValues())  # Output: [1, 3]

# my_linked_list.insertHead(5)
# print(my_linked_list.getValues())

# my_linked_list.insertTail(6)
# print(my_linked_list.getValues())

print(my_linked_list.remove(1))

my_linked_list.insertTail(2)
# print(my_linked_list.getValues())  # Output: [1, 2, 3]

print(my_linked_list.get(1))  # 2
print(my_linked_list.get(0))  # 2


# answer version：
# 提供的答案从一开始的初始化链表就不一样了所以不能全盘照抄，要自己理解了，然后写自己的代码

# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Implementation for Singly Linked List


class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
