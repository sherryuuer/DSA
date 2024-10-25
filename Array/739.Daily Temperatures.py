# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have
# to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
# 0,  1,  2,  3,  4,  5,   6,   7
# Output: [1,1,4,2,1,1,0,0]

temperatures2 = [30, 40, 50, 60]
# Output: [1,1,1,0]

# solution1: brute force
# step:
# prepare: answer = []
# 1, loop i in range(0 ~ len(t) - 1)
# 2, loop j = i + 1 find a element bigger than i
# 3, answer[i] = j - i
# 4, return answer
# ----- time O(n^2), space O(n)

# solution2: stack to reduce the time and space to O(n)
# step:
# edge case: [] return []
# prepare: stack = [(t[0], 0),], result = [0 for _ in range(len(t))]
# 1, loop i in range(1, len(t) - 1)
# 2, while t[i] > stack[-1]: stack.pop(), result[index] = i - index, stack.append(t[i])
# 3, while stack is not empty: stack.pop(), result[index] = 0
# 4, return result


def dailyTemperatures(t):
    if not t:
        return []

    stack = [[t[0], 0],]
    result = [0 for _ in range(len(t))]

    for i in range(1, len(t)):  # 一种转换视角从被比较者的角度重构问题
        while stack and t[i] > stack[-1][0]:  # temp
            _, index = stack.pop()
            result[index] = i - index
        stack.append([t[i], i])

    return result


# test
print(dailyTemperatures(temperatures1))
