class SnapshotArray_memoryout(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.snapshot = {}  # id:array
        self.array = [0] * self.length
        self.curid = -1

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.curid += 1
        self.snapshot[self.curid] = self.array[:]
        return self.curid

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        print(self.snapshot)
        return self.snapshot[snap_id][index]


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [[[-1, 0]] for _ in range(length)]
        self.snapid = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index].append([self.snapid, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snapid += 1
        return self.snapid - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        import bisect
        # print(self.array)
        i = bisect.bisect(self.array[index], [snap_id+1])-1
        return self.array[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
obj.set(0, 6)
obj.set(0, 7)
param_3 = obj.snap()
obj.set(1, 4)
param_3 = obj.get(1, 1)
print(param_3)
