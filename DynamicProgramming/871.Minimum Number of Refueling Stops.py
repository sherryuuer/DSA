def min_refuel_stops(target, start_fuel, stations):
    # dp[i]表示在加满i次油的情况下，能到达的最远距离
    dp = [start_fuel] + [0] * len(stations)
    for i in range(len(stations)):
        for j in range(i, -1, -1):

            if dp[j] >= stations[i][0]:
                dp[j + 1] = max(dp[j + 1], dp[j] + stations[i]
                                [1])  # i = 2, j = 1
            print(i, j, dp)
    for i in range(len(dp)):
        if dp[i] >= target:
            return i

    return -1


stations = [[2, 5], [3, 1], [6, 3], [12, 6]]
target = 15
start_fuel = 3
res = min_refuel_stops(target, start_fuel, stations)
print(res)
# - dp[3, 8, 11, 12, 18]  # 在该点可以去的最大距离
#    dist[2, 3, 6, 12]
#    fuel[5, 1, 3,  6]
