# https://leetcode.com/problems/course-schedule-iv/description/


class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        preMap = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        def dfs(crs, pre, visit):
            if crs == pre:
                return True

            visit.add(crs)
            for p in preMap[crs]:
                if p not in visit and dfs(p, pre, visit):
                    return True
            return False

        ans = []
        for c, p in queries:
            visit = set()
            ans.append(dfs(c, p, visit))
        return ans


numCourses = 3
prerequisites = [[1, 2], [1, 0], [2, 0]]
queries = [[1, 0], [1, 2]]
# Output: [true,true]
solution = Solution()
res = solution.checkIfPrerequisite(numCourses, prerequisites, queries)
print(res)

# 下面是一种找到所有的先修课程的方法


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre)
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}  # map course -> set indirect prereqs
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
