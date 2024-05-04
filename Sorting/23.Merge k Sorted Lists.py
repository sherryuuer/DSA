# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            cur = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1:
                cur.next = list1
            elif list2:
                cur.next = list2
            return dummy.next

        n = len(lists)
        if n == 0:
            return None

        L = lists[0]
        if n > 1:
            for i in range(1, n):
                L = mergeTwoLists(L, lists[i])
        return L

        # n = len(lists)
        # middle = n // 2
        # left = lists[:middle]
        # right = lists[middle:]
        # return mergeTwoLists(self.mergeKLists(left), self.mergeKLists(right))
