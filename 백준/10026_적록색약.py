from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * n for _ in range(n)]


def bfs(x, y, color):
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == color:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))


def check(color):
    count = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and graph[y][x] == color:
                bfs(x, y, color)
                count += 1
    return count


print(check('R')+check('G')+check('B'), end=' ')

visited = [[False] * n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if graph[y][x] == 'G':
            graph[y][x] = 'R'

print(check('R')+check('B'))