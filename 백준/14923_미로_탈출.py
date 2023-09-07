import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
hy, hx = map(int, input().split())
ey, ex = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((hx - 1, hy - 1, 0))

    while q:
        x, y, z = q.popleft()

        if x == ex - 1 and y == ey - 1:
            print(visited[y][x][z])
            return
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 < ny < n:
                if graph[ny][nx] == 1 and z == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((nx, ny, 1))
                elif graph[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((nx, ny, z))

    print(-1)
    return

bfs()