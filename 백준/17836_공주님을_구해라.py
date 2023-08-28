from collections import deque
import sys

n, m, t = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
visited = [[0] * m for _ in range(n)]
visited[n-1][m-1] = sys.maxsize
for _ in range(n):
    graph.append(list(map(int, input().split())))

gram_T = 0
queue = deque([(0, 0)])
while len(queue) > 0:
     x, y = queue.popleft()
     if graph[y][x] == 2: # 검 발견
         gram_T = visited[y][x] + (n - y - 1) + (m - x - 1)
     for i in range(4):
         nx = dx[i] + x
         ny = dy[i] + y
         if 0 <= nx < m and 0 <= ny < n:
             if (visited[ny][nx] == 0 or visited[ny][nx] == sys.maxsize) and graph[ny][nx] != 1: # 방문하지 않았다면
                 visited[ny][nx] = visited[y][x] + 1
                 queue.append((nx, ny))

v = min(visited[n-1][m-1], gram_T)
if v == 0 or v > t:
    print('Fail')
else:
    print(v)