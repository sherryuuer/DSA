# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
# Output: 3


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))

            if not sandwiches or sandwiches[0] not in students:
                return len(students)


s = Solution()
print(s.countStudents(students, sandwiches))
