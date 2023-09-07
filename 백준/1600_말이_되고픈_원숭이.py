import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1]
dy = [0, 0, 1, -1, 2, 1, -1, -2, -2, -1, 1, 2]

visited = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()

        if a == m - 1 and b == n - 1:
            return visited[a][b][c]

        for i in range(12):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0 and i < 4:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

            elif graph[nx][ny] == 0 and visited[nx][ny][c - 1] == 0 and c > 0 and i >= 4:
                visited[nx][ny][c - 1] = visited[a][b][c] + 1
                queue.append((nx, ny, c - 1))


    return -1


print(bfs(0, 0, k))
