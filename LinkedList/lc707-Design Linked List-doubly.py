# https://leetcode.com/problems/design-linked-list/
# 双向链表
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val)

        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        读题！！
        If index equals the length of the linked list,
        the node will be appended to the end of the linked list.
        If index is greater than the length,
        the node will not be inserted.
        必须考虑全部的情况
        """
        node = ListNode(val)
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                if curr != self.tail:
                    tmp = curr.prev
                    node.next = curr
                    curr.prev = node
                    node.prev = tmp
                    tmp.next = node
                    return
                elif curr == self.tail:
                    self.addAtTail(val)
                    return
            curr = curr.next
            i += 1

        return -1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head.next
        i = 0
        while curr:
            if i == index and curr.next:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            curr = curr.next
            i += 1

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtIndex(1, 0)
print("add at index 1 with 0")
print(obj.getValues())

param_1 = obj.get(0)
print(param_1)


# ------------pass
# obj.addAtHead(1)
# print(obj.getValues())

# obj.addAtTail(3)
# print(obj.getValues())

# obj.addAtIndex(1, 2)
# print("add at index 1 with 2")
# print(obj.getValues())

# param_1 = obj.get(1)
# print(param_1)


# ------------pass
# obj.addAtHead(7)
# print("add head 7")
# print(obj.getValues())

# obj.addAtHead(2)
# print("add head 2")
# print(obj.getValues())

# obj.addAtHead(1)
# print("add head 1")
# print(obj.getValues())

# obj.addAtIndex(3, 0)
# print("add at index 3 with 0")
# print(obj.getValues())

# obj.deleteAtIndex(2)
# print("delete val at index 2")
# print(obj.getValues())

# obj.addAtHead(6)
# print(obj.getValues())

# obj.addAtTail(4)
# print(obj.getValues())

# param_1 = obj.get(4)
# print(param_1)
# obj.addAtHead(4)
# obj.addAtIndex(5, 0)
# obj.addAtHead(6)
# expect: [null, null, null, null, null, null, null, null, 4, null, null, null]
