def AlienDictionary(words):
    adj = {char: set() for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
            return ""

        for j in range(minlen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visit = {}
    res = []

    def dfs(char):
        if char in visit:
            return visit[char]

        visit[char] = True
        for nei in adj[char]:
            if dfs(nei):
                return True

        visit[char] = False
        res.append(char)

    for char in adj:
        if dfs(char):
            return ""

    res.reverse()
    return "".join(res)


def AlienDictionary(words):
    adj = {char: set() for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
            return ""

        for j in range(minlen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    topSort = []
    cycle, visit = set(), set()

    def dfs(i):
        if i in cycle:
            return False
        if i in visit:
            return True

        cycle.add(i)
        for neighbor in adj[i]:
            if not dfs(neighbor):
                return False
        cycle.remove(i)
        visit.add(i)
        topSort.append(i)
        return True
    for char in adj:
        if not dfs(char):
            return ""
    return "".join(topSort)
