# 0은 이동할 수 있는 곳
# 1은 이동할 수 없는 벽
# (1,1)에서 (N, M)의 위치까지 이동 -> 최단 경로?
# 벽 한개까지 부수고 이동하기 가능
# 상하좌우로 인접

# 최단경로 = BFS
# 한칸씩 부숴서 탐색, 안부신거 탐색..
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


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
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))

# visited[x][y][0] : (x, y)까지 벽을 뚫지 않고 왔을 때
# visited[x][y][1] : (x, y)까지 벽을 한번이라도 뚫고 온 경우
