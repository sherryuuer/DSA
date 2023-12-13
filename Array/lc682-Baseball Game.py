# https://leetcode.com/problems/baseball-game/
# An integer x.Record a new score of x.
# '+'.Record a new score that is the sum of the previous two scores.
# 'D'.Record a new score that is the double of the previous score.
# 'C'.Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.


class mySolution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stacks = []
        for op in operations:
            try:
                op = int(op)
                stacks.append(op)
            except ValueError:
                if op == '+':
                    stacks.append(stacks[-1] + stacks[-2])
                elif op == 'D':
                    stacks.append(2 * stacks[-1])
                elif op == 'C':
                    stacks.pop()
        return sum(stacks)

    def calPoints2(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stacks = []
        for op in operations:
            if op == '+' and len(stacks) >= 2:
                stacks.append(stacks[-1] + stacks[-2])
                print(stacks)
            elif op == 'D' and len(stacks) >= 1:
                stacks.append(2 * stacks[-1])
                print(stacks)
            elif op == 'C' and len(stacks) >= 1:
                stacks.pop()
                print(stacks)
            else:
                stacks.append(int(op))
        return sum(stacks)


myso = mySolution()
res = myso.calPoints2(ops)
print(res)
