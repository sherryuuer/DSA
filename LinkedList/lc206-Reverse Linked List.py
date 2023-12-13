# https://leetcode.com/problems/reverse-linked-list/

# head = [1, 2, 3, 4, 5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 方法一，双指针
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # two pointer
        prev, cur = None, head

        while cur:
            # keep the cur.next in a val(the val behind the cur pointer)
            tmp = cur.next
            # turn the cur pointer node to point to prev
            cur.next = prev
            # move the prev pointer to cur
            prev = cur
            # cur pointer will move to the old cur.next
            cur = tmp
        # at last ,the cur will be None ,and the prev will be the head
        return prev


# 方法二， 递归
# https://www.youtube.com/watch?v=G0_I-ZF0S38
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # T O(n) M O(n)
        if not head:
            return None

        newHead = head
        while head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
