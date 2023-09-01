from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n + 2)]
for _ in range(m):
    graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0] * (n + 2))

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]

visited = [[False] * (n + 2) for _ in range(m + 2)]


def bfs(i, j):
    cnt = 0
    queue = deque()
    queue.append((i, j))
    visited[j][i] = True
    while queue:
        x, y = queue.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[y % 2][i]

            if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                elif graph[ny][nx] == 1:
                    cnt += 1
    return cnt

print(bfs(0, 0))
