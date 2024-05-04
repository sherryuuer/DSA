# https://leetcode.com/problems/k-closest-points-to-origin/description/
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        minheap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            minheap.append((distance, point[0], point[1]))
        heapq.heapify(minheap)
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(minheap)
            res.append([x, y])
        return res


class Solution2(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        pdict = {}
        for p in points:
            distance = p[0]**2 + p[1]**2
            if distance not in pdict:
                pdict[distance] = [p]
            else:
                pdict[distance].append(p)
        print(pdict)

        keylst = list(pdict.keys())
        heapq.heapify(keylst)
        res = []
        count = 0
        while count < k:
            key = heapq.heappop(keylst)
            res += pdict[key]
            count += len(pdict[key])

        return res


points = [[0, 1], [1, 0]]
k = 2
s = Solution()
print(s.kClosest(points, k))
