from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

m, n, h = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
for z in range(h):
    temp = []
    for y in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(temp)

day = 0
def bfs():
    while len(queue) > 0:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:  # 익지 않은 토마토면
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nx, ny, nz))

ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
               queue.append((x, y, z))

bfs()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                print(-1)
                exit(0)
            day = max(day, graph[z][y][x])
print(day-1)