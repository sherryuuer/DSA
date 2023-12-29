class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self):
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # move the last val to the top
        self.heap[1] = self.heap.pop()
        i = 1

        # Percolate down
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
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def heapify(self, arr):
        # make the arr 's 0 th element to the end to make it a heap
        # arr.append(arr[0])  # this will cause index out of range
        arr = [0] + arr
        # now it is heap
        self.heap = arr
        # there are only half nodes have children
        # 从上往下推比，从下往上更有效率，因为可以省掉一半的， 没有child的nodes
        cur = len(self.heap) // 2

        # Percolate down
        while cur > 0:
            i = cur

            # Percolate down
            while i * 2 < len(self.heap):  # at least have the left child
                # have the right , and right child is least than root and left
                if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i * 2 + 1] < self.heap[i]:
                    # swap root with the right
                    self.heap[i], self.heap[i * 2 +
                                            1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                # left is least than the root
                elif self.heap[i * 2] < self.heap[i]:
                    self.heap[i], self.heap[i *
                                            2] = self.heap[i * 2], self.heap[i]
                    i = i * 2
                # at the right position
                else:
                    break

            cur -= 1


# rewrite the percolate up and down
class MinHeap:
    def __init__(self):
        self.heap = [0]

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
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # move the last val to the top
        self.heap[1] = self.heap.pop()
        i = 1

        # Percolate down
        self._percolate_down(i)
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def heapify(self, arr):
        # make the arr 's 0 th element to the end to make it a heap
        # arr.append(arr[0])  # this will cause index out of range
        arr = [0] + arr
        # now it is heap
        self.heap = arr
        # there are only half nodes have children
        # 从上往下推比，从下往上更有效率，因为可以省掉一半的， 没有child的nodes
        cur = len(self.heap) // 2

        # Percolate down
        while cur > 0:
            i = cur

            # Percolate down
            self._percolate_down(i)

            cur -= 1
