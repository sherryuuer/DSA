# Find Median
# small is a Maxheap, large is a Minheap
import heapq


class Median:
    def __init__(self):
        self.small = []
        self.large = []

    def insert(self, num):
        # push it in to the small(Maxheap), swap if needed
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # handle the balance
        if len(self.small) > len(self.large):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def getMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
