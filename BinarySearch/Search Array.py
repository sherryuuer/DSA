arr = [1, 3, 3, 4, 5, 6, 7, 8]
target = 7


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if target < arr[middle]:
            right = middle - 1
        elif target > arr[middle]:
            left = middle + 1
        else:
            return middle
    return -1


res = binary_search(arr, target)
print(res)
