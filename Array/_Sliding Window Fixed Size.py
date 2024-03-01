# give an array, return true if there are two element within a window of size K
# that are equal


# Check if array contains a pair of duplicate values,
# where the two duplicates are no farther than k positions from
# eachother (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
# O(n * k)
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        print(L)
        print("----")
        for R in range(L + 1, min(len(nums), L + k)):
            print(R)
            if nums[L] == nums[R]:
                return True
    return False


# some problems using sliding window
# O(n)
def closeDuplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


# 给定这个定数的窗口，循环列表，当超过了k就将左边的移除同时移动左指针一下，右边指针的数字如果在窗口中直接返回真

nums = [1, 3, 4, 5, 3]
k = 2
# closeDuplicatesBruteForce(nums, k)

for i in range(5, 3):
    print(i)
