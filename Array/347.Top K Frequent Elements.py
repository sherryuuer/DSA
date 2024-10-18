nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]


class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq

        countMap = Counter(nums)
        lst = [(v * -1 , k) for k, v in countMap.items()]
        heapq.heapify(lst)

        res = []
        for i in range(k):
            res.append(heapq.heappop(lst)[1])

        return res


solution = Solution()
res = solution.topKFrequent(nums, k)
print(res)
