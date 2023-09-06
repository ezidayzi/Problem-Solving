import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny][c - 1] == 0 and c > 0:
                visited[nx][ny][c - 1] = visited[a][b][c] + 1
                queue.append((nx, ny, c - 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, k))
