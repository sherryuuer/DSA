# https://leetcode.com/problems/design-linked-list/

# 单link做的不好，选择单的做一下
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                print(curr.value)
                return curr.value
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 为什么不需要存储阶段的head呢，因为本来就在初始中，不会丢弃，而倒数第二个和第二个就会找不到
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        curr = self.head
        i = 0
        while curr:
            if i == index:
                if curr.next != self.tail:
                    tmp = curr.next
                    curr.next = node
                    node.next = tmp
                    return
                elif curr.next == self.tail:
                    self.addAtTail(val)
            curr = curr.next
            i += 1
        return -1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.head
        i = 0
        while curr and index > 0:
            if i == index and curr.next:
                curr.next = curr.next.next
                return
            curr = curr.next
            i += 1
        if curr.next == self.tail and index == 0:
            self.head.next = self.tail

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
print("add head 7")
print(obj.getValues())

obj.addAtHead(2)
print("add head 2")
print(obj.getValues())

obj.addAtHead(1)
print("add head 1")
print(obj.getValues())

obj.addAtIndex(3, 0)
print("add at index 3 with 0")
print(obj.getValues())

obj.deleteAtIndex(2)
print("delete val at index 2")
print(obj.getValues())

obj.addAtHead(6)
print(obj.getValues())

obj.addAtTail(4)
print(obj.getValues())

param_1 = obj.get(4)
print(param_1)
obj.addAtHead(4)
obj.addAtIndex(5, 0)
obj.addAtHead(6)
# expect : [null,null,null,null,null,null,null,null,4,null,null,null]
