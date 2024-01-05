# Floyd's Tortoise and Hare Algorithm
# 弗洛伊德龟兔算法
# Find the middle of a linked list.
# Time O(n), Space O(1)
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
# 由于上述条件是fast和他的下一个都有，所以覆盖了所有的奇数和偶数条件
# 奇数的情况fast到达最后一个，slow到达中位
# 偶数的情况fast到达None，slow到达第二中位

# 判断是否是一个循环链表
# 普通可以用一个hashset判断是否元素重复
# 如何优化？


def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 判断是否是一个循环，然后返回这个head
# 当快慢指针重合的时候，忘记快针，从起点重生一个slow2指针
# 两个慢指针重合的地方就是循环的起点
# 解释是数学距离问题


def hasCycle2(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
