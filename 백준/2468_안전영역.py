import sys

sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 0 and graph[nx][ny] > h:
            dfs(nx, ny, h)


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

ans = 0

for i in range(0, 101):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and graph[x][y] > i:
                count += 1
                dfs(x, y, i)

    ans = max(count, ans)
print(ans)