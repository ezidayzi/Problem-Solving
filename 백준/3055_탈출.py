from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))

q = deque()
water = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'S':
            q.append((x, y, 0))
        if graph[y][x] == '*':
            water.append((x, y, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * m for _ in range(n)]


def spread(t):
    while water:
        wx, wy, wt = water.popleft()
        if t < wt:
            water.appendleft((wx, wy, wt))
            return
        for i in range(4):
            nx = wx + dx[i]
            ny = wy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == '.':
                    water.append((nx, ny, wt + 1))
                    graph[ny][nx] = '*'


while q:
    x, y, t = q.popleft()
    spread(t)

    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, t + 1))

            if graph[ny][nx] == 'D':
                print(t + 1)
                exit(0)

print("KAKTUS")
