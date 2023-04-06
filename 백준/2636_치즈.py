# 1. 0인 테두리를 따라서 bfs 돈다
# 2. 돌면서 주변에 1이 있으면 녹일 치즈로 판단하고 배열에 넣음
# 3. 치즈 배열 반환.
# 4. 치즈 배열에 아무것도 안담길때까지
# 5. 반환받은 치즈 배열로 0으로 녹임

from collections import deque

n, m = list(map(int, input().split())) # 세로 가로
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    cheese = []
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx] == 0: # 테두리 돌기
                    queue.append((nx, ny))
                if not visited[ny][nx] and graph[ny][nx] == 1: # 치즈면
                    cheese.append((nx, ny))
                visited[ny][nx] = True


    return cheese

day = 0
history = []

while True:
    cheese = []

    visited = [[False] * m for _ in range(n)]

    c = bfs(0, 0)
    if len(c) > 0:
        cheese.append(c)

    if not cheese: # 더 이상 녹을 치즈가 없으면
        break

    history = []
    for c in cheese:
        for (x, y) in c:
            graph[y][x] = 0 # 치즈 녹게 만들기
            history.append(c)

    day += 1


print(day)
print(len(history))