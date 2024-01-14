# https://leetcode.com/problems/linked-list-cycle-ii/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # 这段代码一定要在巡回完了之后进行。表示判断没有循环，并且链表只有一个节点
        if not fast or not fast.next:
            return None

        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        return slow
