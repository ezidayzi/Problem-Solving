import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))

data.sort()
q = deque(data)

S, X, Y = map(int, input().split())

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while q:
    v, x, y, t = q.popleft()
    if t == S:
        break

    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((v, nx, ny, t + 1))

print(graph[X-1][Y-1])