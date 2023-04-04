# 하나의 토마토의 인접한곳 -> 왼, 오, 앞, 뒤 네ㅏㅇ향
# 며칠이 지나야 토마토들이 모두 익는지 최소 일수
# 보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들이 영향을 받아 익게 됨
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1 토마토가 없음

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

m, n = list(map(int, input().split()))
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:  # 익은 토마토 발견
            queue.append((x, y))


while len(queue) > 0:
    x, y = queue.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 0:  # 익지 않은 토마토면
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

isZero = False

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            isZero = True

if isZero:
    print(-1)
else:
    maxDay = max([max(row) for row in graph])
    if maxDay <= -1: # 토마토가 모두 익지 못하는 상황이면
        print(-1)
    else:
        print(maxDay-1)
