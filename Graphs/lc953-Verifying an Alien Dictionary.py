class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        char_dict = {c: idx for idx, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            inner_break = False
            for j in range(min(len(word1), len(word2))):
                if word1[j] == word2[j]:
                    continue
                elif char_dict[word1[j]] < char_dict[word2[j]]:
                    inner_break = True
                    break  # break current inner loop
                else:
                    return False

            if not inner_break and len(word2) < len(word1):
                return False

        return True


words = ["apap", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
solution = Solution()
res = solution.isAlienSorted(words, order)
print(res)


# 其他好的解法
def verify_alien_dictionary(words, order):
    if len(words) == 1:
        return True

    order_map = {}

    for index, val in enumerate(order):
        order_map[val] = index

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            # 当顺次可以比较到这个位置的时候，会触发长度判断
            if j >= len(words[i + 1]):
                return False

            if words[i][j] != words[i + 1][j]:
                if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                    return False
                # 否则打断循环继续下一组单词比较
                break

    return True
