from collections import deque
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph1 = []
for i in range(n):
    graph1.append(list(map(int, input().split())))

ans = 0
def make_wall(count):
    global ans
    if count == 3:
        ans = max(ans, bfs())
        return
    for i in range(n):
        for k in range(m):
            if graph1[i][k] == 0:
                graph1[i][k] = 1
                make_wall(count + 1)
                graph1[i][k] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    graph = copy.deepcopy(graph1)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((j, i))
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 바이러스 퍼뜨리기
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 0:  # 빈칸이면
                    graph[ny][nx] = 2
                    queue.append([nx, ny])

    cnt = 0
    for i in graph:
        cnt += i.count(0)
    return cnt

make_wall(0)
print(ans)