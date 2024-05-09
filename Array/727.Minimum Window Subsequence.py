def min_window(S, T):
    n = len(S)
    m = len(T)

    start = -1  # 记录最小窗口子序列的起始位置
    minLen = float('inf')  # 记录最小窗口子序列的长度

    i = 0
    j = 0

    while i < n:
        if S[i] == T[j]:
            j += 1  # 在T中找到一个字符，向后移动T的指针
            if j == m:  # 如果T的指针已经到达末尾，即找到一个包含T的子序列
                end = i  # 记录当前窗口的结束位置
                j -= 1  # 回退T的指针，以便找到最小窗口子序列

                # 向前移动T的指针，直到不再满足条件
                while j >= 0:
                    if S[i] == T[j]:
                        j -= 1
                    i -= 1
                i += 1  # 退回到满足条件的位置

                # 计算当前窗口子序列的长度，并更新最小窗口的起始位置和长度
                if end - i + 1 < minLen:
                    minLen = end - i + 1
                    start = i
                # 这里很重要，要把j重制到开头，以便下一次遍历和比较
                j = 0
        i += 1

    if start == -1:
        return ""
    else:
        return S[start: start + minLen]


min_window("abcdbebe", "bbe")
