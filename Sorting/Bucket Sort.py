arr = [2, 1, 2, 0, 0, 2]


def bucket_sort(arr):
    counts_num = len(set(arr))
    counts = [0] * counts_num
    # print(counts)
    for n in arr:
        counts[n] += 1
    # print(counts)
    i = 0  # for insert the number in the arr's index
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


res = bucket_sort(arr)
print(res)
