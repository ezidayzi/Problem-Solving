from collections import deque

dx = [1, -1, 0, 0]  # 좌우
dy = [0, 0, 1, -1]  # 상하

count = 0

def bfs(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 1
    size = 1

    while len(queue) > 0:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((nx, ny))
                size += 1

    return size


m, n, k = list(map(int, input().split())) # 세로, 가로

arr = [[] for _ in range(k)]
for i in range(k):
    arr[i] = list(map(int, input().split())) # 왼쪽 아래 꼭짓점의 x, y & 오른쪽 위 꼭짓점의 x, y

graph = [[0 for _ in range(n)] for _ in range(m)]

for s in arr:
    leftX = s[0]
    leftY = s[1]
    rightX = s[2]
    rightY = s[3]

    for x in range(leftX, rightX):
        for y in range(leftY, rightY):
            graph[y][x] = 1

answer = []

for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            answer.append(bfs(x, y))
            count += 1

print(count)
answer.sort()
for a in answer:
    print(a, end =' ')