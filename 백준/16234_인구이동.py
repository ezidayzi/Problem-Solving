import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 좌 우
dy = [0, 0, -1, 1] # 하 상

n, l, r = list(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    union = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if l <= abs(graph[ny][nx] - graph[y][x]) <= r: # 조건을 만족할 때
                    visited[ny][nx] = True
                    union.append((nx, ny)) # union 배열에 넣기
                    queue.append((nx, ny))

    return union


ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    unions = []

    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                union = bfs(x, y)
                if len(union) > 1:
                    unions.append(union)

    if not unions: # 더 이상 인구 이동이 일어나지 않으면
        break

    ans += 1

    # 인구 업데이트
    for union in unions:
        pop = sum([graph[y][x] for x, y in union]) // len(union)
        for x, y in union:
            graph[y][x] = pop

print(ans)
