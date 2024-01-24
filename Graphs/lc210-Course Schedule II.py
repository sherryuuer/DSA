# https://leetcode.com/problems/course-schedule-ii/description/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap = {c: [] for c in range(numCourses)}
        # c : course; p: prerequisites
        for c, p in prerequisites:
            preMap[c].append(p)
        print(preMap)

        visit, cycle = set(), set()
        topSort = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            # print(f"cycle: {cycle} ")
            for pre in preMap[c]:
                if not dfs(pre):
                    return False

            cycle.remove(c)
            visit.add(c)
            topSort.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return topSort


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output: [0,2,1,3]
solution = Solution()
res = solution.findOrder(numCourses, prerequisites)
print(res)
