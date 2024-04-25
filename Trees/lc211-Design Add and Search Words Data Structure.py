# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# 和原本的前缀树的不同是，加入了一个点可以取代任何字母的设定


class TrieNode:

    def __init__(self):

        self.children = {}
        self.word = False


class WordDictionary(object):

    def __init__(self):

        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def helper(self, word, cur):
        for i in range(len(word)):
            if word[i] == ".":
                for child in cur.children.values():
                    # 这里的分支判断很重要，可以避免最后一个是点的情况，出现错误的结果，这么看来网友的好多测试用例真的蛮有用的，避免了很多bug
                    if self.helper(word[i + 1:], child):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False

                cur = cur.children[word[i]]
        return cur.word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        return self.helper(word, cur)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# 其他题解
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


# 加入了get words方法：

class TrieNode:
    def __init__(self, val=None):
        self.children = {}
        self.word = False
        self.val = val


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = True

    def search_word(self, word):
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

    def get_words(self):
        def dfs(cur, curset, subsets):
            curset.append(cur.val)
            if cur.word:
                subsets.append(''.join(curset))
            # 嵌套字典
            for child in cur.children.values():
                dfs(child, curset, subsets)
            curset.pop()

        result = []
        for cur in self.root.children.values():
            dfs(cur, [], result)
        return result


obj = WordDictionary()
obj.add_word("bad")
obj.add_word("dad")
obj.add_word("mad")
print(obj.get_words())
print(obj.search_word(".ad"))
