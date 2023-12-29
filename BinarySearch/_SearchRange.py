# 一个二元查找的模板在一个range中是否存在target值
def is_correct(target, n):
    if n > target:
        return 1
    elif n < target:
        return -1
    else:
        return 0


def binary_search(low, high, n, target):

    while low <= high:
        middle = (low + high) // 2

        if is_correct(middle) > 0:
            high = middle - 1
        elif is_correct(middle) < 0:
            low = middle + 1
        else:
            return middle
    return -1

# O(logn)
