# https://leetcode.com/problems/accounts-merge/description/


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += p1
        return True


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        uf = UnionFind(len(accounts))
        emailToAcc = {}  # email to index of account

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(idx, emailToAcc[email])
                else:
                    emailToAcc[email] = idx

        emailGroup = defaultdict(list)
        for email, idx in emailToAcc.items():
            user = uf.find(idx)
            emailGroup[user].append(email)

        res = []
        for idx, email in emailGroup.items():
            name = accounts[idx][0]
            res.append([name] + sorted(email))

        return res

# emailToAccount:{'johnsmith@mail.com': 0, 'john_newyork@mail.com': 0,
#                'john00@mail.com': 1, 'mary@mail.com': 2, 'johnnybravo@mail.com': 3}
# uf.par: [0,0,2,3]
# emailGroup:defaultdict(<class 'list'>, {0: ['johnsmith@mail.com',
#           'john_newyork@mail.com', 'john00@mail.com'], 2: ['mary@mail.com'], 3: ['johnnybravo@mail.com']})


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
solution = Solution()
res = solution.accountsMerge(accounts)
print(res)



`defaultdict` 是 Python 中 `collections` 模块中的一种字典（dict）的变体。它与普通字典（`dict`）的区别在于，`defaultdict` 允许你为字典的键指定默认值类型，当访问不存在的键时，会自动为该键创建默认值。

以下是 `defaultdict` 的基本用法：

```python
from collections import defaultdict

# 创建一个 defaultdict，并指定默认值类型为 int
my_dict = defaultdict(int)

# 访问不存在的键，会自动创建并初始化为默认值 0
my_dict['a'] += 1
my_dict['b'] += 2

print(my_dict)  # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
```

在上面的例子中，`defaultdict` 的默认值类型被设置为 `int`，因此当访问字典中不存在的键时，会自动创建一个新的键，并将其默认值初始化为 0。这样就避免了在使用普通字典时需要在每次访问前检查键是否存在的麻烦。

你可以将任何可调用对象（例如函数或类）作为默认值类型，以便更复杂的初始化逻辑。例如：

```python
from collections import defaultdict

# 创建一个 defaultdict，并指定默认值类型为 list
my_dict = defaultdict(list)

# 访问不存在的键，会自动创建并初始化为空列表
my_dict['a'].append(1)
my_dict['b'].append(2)

print(my_dict)  # 输出: defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
```

这使得 `defaultdict` 在某些情况下非常方便，特别是在处理计数或分组等任务时。
