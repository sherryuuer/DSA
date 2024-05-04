# https://leetcode.com/problems/course-schedule/description/
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# Output: false


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if premap[c] == []:
                return True

            visit.add(c)
            for pre in premap[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            premap[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


solution = Solution()
res = solution.canFinish(numCourses, prerequisites)
print(res)
