from collections import deque
from collections import defaultdict

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
group_num = 2


def bfs(i, j):
    queue.append((i, j))
    cnt = 0
    while len(queue) > 0:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = group_num
    return cnt

group = defaultdict()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            graph[y][x] = group_num
            group[group_num] = bfs(x, y)
            group_num += 1

max_size = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            size = set()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] >= 2:
                    size.add(graph[ny][nx])
            sum_size = 0
            for s in size:
                sum_size += group[s]
            max_size = max(max_size, sum_size)


print(max_size+1)