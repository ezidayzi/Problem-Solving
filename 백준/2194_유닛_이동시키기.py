from collections import deque
from sys import stdin

input = stdin.readline

n, m, a, b, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

walls = []
for _ in range(k):
    y, x = map(int, input().split())
    graph[y-1][x-1] = -1
    walls.append((x-1, y-1))
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def check(i, j):
    for x, y in walls:
        if i <= x < i + b and j <= y < j + a:
            return False
    return True


def bfs():
    q = deque()
    q.append((sx - 1, sy - 1))

    while q:
        x, y = q.popleft()

        if y == ey - 1 and x == ex - 1:
            print(visited[y][x])
            return

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= nx < m and 0 <= ny < n and 0 <= nx + b - 1 < m and 0 <= ny + a - 1 < n:
                if visited[ny][nx] == 0:
                    if check(nx, ny):
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((nx, ny))

    print(-1)
    return


bfs()
