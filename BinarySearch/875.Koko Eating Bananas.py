# https://leetcode.com/problems/koko-eating-bananas/description/

import math
piles = [3, 6, 7, 11]
h = 8
# output 4 the min k = nums/h

# piles = [30, 11, 23, 4, 20]
# h = 5
# Output: 30
# print(math.ceil(7/4))

# piles = [30, 11, 23, 4, 20]
# h = 6
# Output: 23

# piles = [312884470]
# h = 968709470
# 考虑这个特殊情况，给到的时间远远大于香蕉数量，有的速度区间会落到0


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        maxk = max(piles)
        mink = 1

        def checkk(piles, h, k):
            hour = 0
            for n in piles:
                hour += math.ceil(float(n)/k)
            if hour > h:
                return False
            else:
                return True

        while mink <= maxk:
            midk = (mink + maxk) // 2
            print(mink, maxk)

            if not checkk(piles, h, midk):
                mink = midk + 1
            elif checkk(piles, h, midk):
                maxk = midk - 1
            else:
                return midk
        return midk
        # else:
        #     if midk == 1 or not checkk(piles, h, midk - 1):
        #         return midk  # 设置短路条件，以防k为0
        #     maxk = midk - 1

        # # this should be right but out of memory.
        # for k in range(mink, maxk + 1):
        #     if checkk(piles, h, k):
        #         return k


solution = Solution()
res = solution.minEatingSpeed(piles, h)
print(res)


# let's do again
class Solution2(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        import math
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for n in piles:
                hours += math.ceil(n / mid)

            if hours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


so2 = Solution2()
res = so2.minEatingSpeed(piles, h)
print(res)
