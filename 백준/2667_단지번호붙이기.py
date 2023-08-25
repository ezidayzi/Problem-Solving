from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]  # 좌우
dy = [0, 0, 1, -1]  # 상하

ans = []
count = 0

def bfs(s, j):
    graph[j][s] = 0
    queue = deque([(s, j)])

    while queue:
        x, y = queue.popleft()
        ans[count - 1] += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx, ny))


for i in range(n): # 가로
    for k in range(n): # 세로
        if graph[k][i] == 1:
            count += 1
            ans.append(0)
            bfs(i, k) # 가로 세로
print(count)
ans.sort()
for i in ans:
    print(i)