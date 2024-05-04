# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# 想像把这个链表对折，node们就是彼此的孪生了
# 孪生值是他们的sum，求最大的sum
# 为什么在快慢指针题中呢，左右指针不是更好？哦因为是链表他只会给你头，所以你要用快慢指针找到中点（快慢指针主要就是用来找中点）
# ？然后我可以反转后半段链表为一个新的链表吗，但我做的其实是给后半段加了prev的属性，但是没有这个属性
# 所以最好的就是将前半段反转为一个反向链表
# 这道题的挑战就是，用到链表的头和尾


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # now the prehalf head is slow.next

        res = slow.val + prev.val
        # [prev : slow, ]slow正好走到后半段的开始，指向的仍然是原来head的next，
        # 重新指向没有被执行，因为fast已经不满足条件了
        cur1, cur2 = prev.next, slow.next
        while cur2:
            res = max(res, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        # # 或者
        # res = 0
        # while slow:
        #     res = max(res, prev.val + slow.val)
        #     prev = prev.next
        #     slow = slow.next
        return res
