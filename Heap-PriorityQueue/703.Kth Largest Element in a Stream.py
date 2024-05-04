# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# 思想就是用只有k个元素的最小堆，保持个数，弹出最小即可

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]


# leetcode's cases are crazy!
class KthLargest_timeout_agein(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        sortednums = sorted(nums)
        self.heap = [0] + sortednums[-k:]
        self.length = k + 1

    def _percolate_up(self, i):
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def _percolate_down(self, i):
        while i * 2 < len(self.heap):  # at least have the left child
            # have the right , and right child is least than root and left
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i * 2 + 1] < self.heap[i]:
                # swap root with the right
                self.heap[i], self.heap[i * 2 +
                                        1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            # left is least than the root
            elif self.heap[i * 2] < self.heap[i]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            # at the right position
            else:
                break

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        self._percolate_up(i)

    def pop(self):
        if len(self.heap) > self.length:

            # move the last val to the top
            self.heap[1] = self.heap.pop()
            i = 1

            # Percolate down
            self._percolate_down(i)

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.push(val)
        self.pop()
        print(self.heap)
        return self.top()


class KthLargest_timeout(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = sorted(nums, reverse=True)
        self.k = k

    def topk(self):
        if len(self.heap) >= self.k + 1:
            return self.heap[self.k]
        return None

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        while i > 0 and self.heap[i] > self.heap[i - 1]:
            self.heap[i], self.heap[i - 1] = self.heap[i - 1], self.heap[i]
            i = i - 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.push(val)
        print(self.heap)

        return self.topk()


# Your KthLargest object will be instantiated and called as such:
kthLargest = KthLargest(3, [4, 5, 8, 2])
res = kthLargest.add(3)   # return 4
print(res)
res = kthLargest.add(5)   # return 5
print(res)
res = kthLargest.add(10)  # return 5
print(res)
res = kthLargest.add(9)   # return 8
print(res)
res = kthLargest.add(4)   # return 8
print(res)
