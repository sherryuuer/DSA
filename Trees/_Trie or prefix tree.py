# Prefix Tree
# Insert word: O(1)
# Search word: O(1)
# Search prefix: O(1)
# 每个枝是一个字母（26个），根据字母可以搜索单词， root是空的
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False  # the end of the word mark


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
