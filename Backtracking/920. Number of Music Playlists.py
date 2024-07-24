# 制约条件1：长度为goal
# 制约条件2：老歌曲必须在k次后再次被使用
# 制约条件3：每首歌都要至少出现一次
# 另外根据题目要求：Since the answer can be very large, return it modulo 10**9 + 7


def numMusicPlaylists(n, goal, k):
    mod = 10**9 + 7

    def helper(cur_goal, used_songs):
        # 如果长度满足，同时用掉了n首歌则是有效列表
        if cur_goal == 0 and used_songs == n:
            return 1
        # 如果上一个if不满足，则在这里判断发现长度满足后，没用掉所有的歌，则说明这题给的条件是无效的
        if cur_goal == 0 or used_songs > n:
            return 0

        # 使用新的歌曲填充列表：新歌数量 * 递归调用（这里用的是新歌所以used数量+1）
        res = (n - used_songs) * helper(cur_goal - 1, used_songs + 1)
        # 使用used歌填充列表：如果used歌曲的长度满足gap长度k，则可以使用，但是这时候used数量不会发生变化
        if used_songs > k:
            res += (used_songs - k) * helper(cur_goal - 1, used_songs)

        return res % mod

    # 递归调用helper函数
    return helper(goal, 0)


# 优化计算，增加一个cache，简化计算量，其他地方和上面相同
def numMusicPlaylists_cached(n, goal, k):
    mod = 10**9 + 7

    # define a cache for values
    cache = {}

    def helper(cur_goal, used_songs):
        if cur_goal == 0 and used_songs == n:
            return 1
        if cur_goal == 0 or used_songs > n:
            return 0
        # check the cache value
        if (cur_goal, used_songs) in cache:
            return cache[(cur_goal, used_songs)]

        res = (n - used_songs) * helper(cur_goal - 1, used_songs + 1)

        if used_songs > k:
            res += (used_songs - k) * helper(cur_goal - 1, used_songs)

        # memorize the value to cache
        cache[(cur_goal, used_songs)] = res % mod
        return cache[(cur_goal, used_songs)]

    return helper(goal, 0)
