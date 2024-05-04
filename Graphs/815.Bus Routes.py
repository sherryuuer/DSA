from collections import deque


def minimum_buses(bus_routes, src, dest):
    stb = {}
    for i in range(len(bus_routes)):
        for station in bus_routes[i]:
            if station not in stb:
                stb[station] = []
            if i not in stb[station]:
                stb[station].append(i)
    visit = set()
    queue = deque([[src, 0],])
    while queue:
        print(queue)
        source, count = queue.popleft()
        if source == dest:
            return count
        if source in stb:
            for bus in stb[source]:
                if bus not in visit:
                    for station in bus_routes[bus]:
                        queue.append([station, count + 1])
                    visit.add(bus)
    return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
res = minimum_buses(bus_routes=routes, src=source, dest=target)
print(res)
