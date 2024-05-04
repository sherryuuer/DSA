def word_break(s, word_dict):
    dp = [[]] * (len(s) + 1)
    dp[0] = [""]

    for i in range(1, len(s) + 1):
        prefix = s[:i]
        temp = []

        for j in range(0, i):
            suffix = prefix[j:]
            if suffix in word_dict:

                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())
        print(temp)
        dp[i] = temp

    return dp[len(s)]


def word_break2(s, word_dict):
    wordset = set(word_dict)

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i] = True
                break

    def backtracking(start, path):
        if start == len(s):
            res.append(" ".join(path))
            return

        for end in range(start + 1, len(s) + 1):
            if dp[end] and s[start:end] in wordset:
                backtracking(end, path + [s[start:end]])

    res = []
    if dp[len(s)]:
        backtracking(0, [])

    return res


s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]

res = word_break(s, word_dict)
print(res)
