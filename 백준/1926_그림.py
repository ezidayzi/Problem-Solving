from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

size = 0


def bfs(x, y):
    global size
    dx = [1, -1, 0, 0]  # 좌우
    dy = [0, 0, 1, -1]  # 상하

    queue = deque([(x, y)])

    c = 1
    while len(queue) > 0:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    c += 1

    size = max(c, size)


cnt = 0

for x in range(m):
    for y in range(n):
        if not visited[y][x] and graph[y][x] == 1:
            visited[y][x] = True
            cnt += 1
            bfs(x, y)

print(cnt)
print(size)
