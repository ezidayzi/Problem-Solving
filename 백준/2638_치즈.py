from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = -1
    cheese = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = -1
                if graph[ny][nx] == 1:
                    visited[ny][nx] += 1
                if visited[ny][nx] >= 2:
                    cheese.append((nx, ny))

    return cheese


day = 0
while True:
    cheese = []

    c = bfs()
    if len(c) > 0:
        cheese.append(c)

    if not cheese:  # 더 이상 녹을 치즈가 없으면
        break

    for c in cheese:
        for (x, y) in c:
            graph[y][x] = 0  # 치즈 녹게 만들기

    day += 1

print(day)
