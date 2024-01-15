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
