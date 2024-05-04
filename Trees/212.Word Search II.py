# https://leetcode.com/problems/word-search-ii/description/
# [["a","a"]] -> "aaa" 网友的边界问题真的绝了，对我们需要一个访问过与否的判断！version2 solution
# 但是还是有的网友的大数据集timeout了，优化！version3优化了这个版本后还是不可以，看来还是要用题解的前缀树数据结构
# 但是version3已经很好了
# 再次学习一下新的版本version4，看来还是要好的数据结构支撑的，所以其实也可以好好优化看似解决了的aoc中的难题。
# 本来version4就很好了但是，case中有一个word列表重复出现单词的情况，所以再次进化一个版本1version5，其实我觉得，没必要重复output重复单词
# 因为在现实中并不好，所以真多不如停留在version4，当然这也要看现实怎么用吧


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution_v5:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution_v4:
    def findWords(self, board, words):
        # build the trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        def _check(r, c, node, word, visit):
            if (
                r < 0 or r == len(board)
                or c < 0 or c == len(board[0])
                or board[r][c] not in node.children
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            # for add word
            word += board[r][c]
            if node.isWord:
                res.append(word)

            locs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for loc in locs:
                _check(loc[0], loc[1], node, word, visit)
            visit.remove((r, c))  # Backtrack！！！注意这一行！

        res = []
        visit = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                _check(r, c, root, "", visit)

        return res


class Solution_v3:
    def findWords(self, board, words):
        def _check(word, r, c, visit):
            if not word:
                return True

            locs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for loc in locs:
                if (
                    0 <= loc[0] < len(board)
                    and 0 <= loc[1] < len(board[0])
                    and word[0] == board[loc[0]][loc[1]]
                    and loc not in visit
                ):
                    visit.add(loc)
                    if _check(word[1:], loc[0], loc[1], visit):
                        return True
                    visit.remove(loc)  # Backtrack！！！注意这一行！

            return False

        def check(word):
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if word[0] == board[r][c]:
                        visit = {(r, c)}
                        if _check(word[1:], r, c, visit):
                            return True
            return False

        return [word for word in words if check(word)]


# Example Usage
board = [["a", "b", "c"],
         ["a", "e", "d"],
         ["a", "f", "g"]]
words = ["eaafgdcba", "eaabcdgfa"]
solution = Solution_v3()
res = solution.findWords(board, words)
print(res)


class Solution_v2(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        M = len(board) + 2
        N = len(board[0]) + 2
        matrix = [[None] * N for _ in range(M)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                matrix[i + 1][j + 1] = board[i][j]

        def _check(word, r, c, visit):
            if not word:
                return True

            locs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for loc in locs:
                if (0 <= loc[0] < M
                    and 0 <= loc[1] < N
                    and word[0] == matrix[loc[0]][loc[1]]
                        and loc not in visit):
                    visit[(loc[0], loc[1])] = 1
                    if _check(word[1:], loc[0], loc[1], visit):
                        return True
                    del visit[loc]  # Backtrack

            return False

        def check(word):

            for r in range(M):
                for c in range(N):
                    if word[0] == matrix[r][c]:
                        visit = {}
                        visit[(r, c)] = 1
                        if _check(word[1:], r, c, visit):
                            return True
            return False

        for word in words:
            if check(word):
                res.append(word)

        return res


board = [["a", "b", "c"],
         ["a", "e", "d"],
         ["a", "f", "g"]]
words = ["eaafgdcba", "eaabcdgfa"]
# Output: []
solution = Solution_v2()
res = solution.findWords(board, words)
print(res)


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        M = len(board) + 2
        N = len(board[0]) + 2
        matrix = [[None] * N for _ in range(M)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                matrix[i + 1][j + 1] = board[i][j]

        def _check(word, r, c):
            if not word:
                return True

            locs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for loc in locs:
                if word[0] == matrix[loc[0]][loc[1]]:
                    if _check(word[1:], loc[0], loc[1]):
                        return True

            return False

        def check(word):

            for r in range(M):
                for c in range(N):
                    if word[0] == matrix[r][c]:
                        if _check(word[1:], r, c):
                            return True
            return False

        for word in words:
            if check(word):
                res.append(word)

        return res


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
# Output: ["eat","oath"]
solution = Solution()
res = solution.findWords(board, words)
print(res)
