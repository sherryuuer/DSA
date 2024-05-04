# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def dfs(self, node, prefix, result):
#         if node.is_end_of_word:
#             result.append(prefix)
#         for char, child in sorted(node.children.items()):
#             self.dfs(child, prefix + char, result)

#     def sort_words(self):
#         result = []
#         self.dfs(self.root, "", result)
#         return result

#     def startWith(self, word, prefix):
#         if len(prefix) > len(word):
#             return False
#         for i in range(len(prefix)):
#             if prefix[i] != word[i]:
#                 return False
#         return True


# def suggested_products(products, search_word):
#     trie = Trie()
#     for word in products:
#         trie.insert(word)
#     words = trie.sort_words()
#     result = []
#     for end in range(1, len(search_word) + 1):
#         prefix = search_word[0:end]
#         lst = []
#         count = 0
#         for word in words:
#             if trie.startWith(word, prefix):
#                 lst.append(word)
#                 count += 1
#                 if count == 3:
#                     break
#         result.append(lst)
#     return result


class TrieNode:
    def __init__(self):
        self.matching_words = []  # 存储匹配的单词列表
        self.children = {}  # 子节点字典


class Trie:
    def __init__(self):
        self.root = TrieNode()  # 创建 Trie 树的根节点

    def insert(self, word):
        # 将单词插入到 Trie 树中
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # 限制每个节点最多存储三个匹配的单词
            if len(node.matching_words) < 3:
                node.matching_words.append(word)

    def search(self, prefix):
        # 搜索与给定前缀匹配的单词
        result, node = [], self.root
        for char in prefix:
            if char not in node.children:
                # 如果前缀不在 Trie 中，则返回空列表
                return result
            node = node.children[char]
        # 返回匹配的单词列表
        return node.matching_words


def suggested_products(products, search_word):
    # 对产品列表进行排序
    products.sort()
    # 创建 Trie 树
    trie = Trie()

    # 将产品插入到 Trie 树中
    for product in products:
        trie.insert(product)

    # 搜索匹配的产品并返回
    result = []
    prefix = ""
    for char in search_word:
        prefix += char
        result.append(trie.search(prefix))
    return result


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
res = suggested_products(products, searchWord)
print(res)
