def word_break(s, word_dict):
    word_dict = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    print(dp)
    return dp[len(s)]


s = 'leetcode'
word_dict = ['leet', 'code']
print(word_break(s, word_dict))
