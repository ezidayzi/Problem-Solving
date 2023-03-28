import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

size = 0

def dfs(x, y):
    global temp
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 < nx <= m and 0 < ny <= n and graph[ny][nx] == 1:
            temp = temp + 1
            graph[ny][nx] = 0
            dfs(nx, ny)

n, m, k = list(map(int, input().split()))
graph = [[0 for _ in range(m+1)] for _ in range(n+1)]

for _ in range(k):
   a, b = list(map(int, input().split()))
   graph[a][b] = 1


for y in range(n+1):
    for x in range(m+1):
        temp = 0
        if graph[y][x] == 1:
            dfs(x, y)
            size = max(temp, size)

print(size)