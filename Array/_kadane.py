arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# O(n^2)
def bruteForce(arr):
    maxSum = arr[0]

    for i in range(len(arr)):
        curSum = 0
        for j in range(i, len(arr)):
            curSum += arr[j]
            maxSum = max(maxSum, curSum)
    return maxSum


# O(n)
def kadane_algorithm(arr):
    curSum = maxSum = arr[0]

    for n in arr[1:]:
        curSum = max(n, curSum + n)
        maxSum = max(curSum, maxSum)
    return maxSum


# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def slidingWindow(arr):
    curSum = maxSum = arr[0]
    maxL, maxR = 0, 0
    L = 0
    for R in range(1, len(arr)):
        if curSum + arr[R] < arr[R]:
            L = R
            curSum = arr[R]
        else:
            curSum = curSum + arr[R]

        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]


result = slidingWindow(arr)
# result = kadane_algorithm(arr)
# result = bruteForce(arr)
print(result)  # 输出 6，对应子数组 [4, -1, 2, 1]
