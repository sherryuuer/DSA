# https://leetcode.com/problems/subarray-sum-equals-k/description/
# 本质是求区间的和，但是这个和会左右变动，又不是有序的，所以双指针x，前缀和算法怎么用。
# 计算出前缀和数组，一种情况是等于k的数字的count，另一种是right-left=k的情况


class Solution_v1(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)

        res = 0
        # 这一段代码在自己run的时候ok，再次提交又遇到超时
        for i, n in enumerate(prefix):
            res += prefix[i + 1:].count(k + n)

        # 双层loop果然超时
        # for m in range(len(prefix) - 1):
        #     for n in range(m + 1, len(prefix)):
        #         if prefix[n] - prefix[m] == k:
        #             res += 1

        res += prefix.count(k)

        return res


class Solution_v2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 果然还是需要哈希表储存结果
        hashmap = {0: 1}  # prefix: count
        total = 0
        res = 0
        for n in nums:
            # 顺序！先计算当前pre然后看是否在字典里，然后添加当前pre
            total += n
            if total - k in hashmap:
                res += hashmap.get((total - k), 0)

            if total not in hashmap:
                hashmap[total] = 1
            else:
                hashmap[total] += 1
            # 或者写成一行
            # hashmap[total] = 1 + hashmap.get(total, 0)

        return res


nums = [1, 1, 1, 1, 1, 1]
k = 0
# Output: 2
solution = Solution_v2()
res = solution.subarraySum(nums, k)
print(res)
