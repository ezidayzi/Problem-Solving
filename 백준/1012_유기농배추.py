from collections import deque

for _ in range(int(input())):
    dx = [1, -1, 0, 0] # 좌우
    dy = [0, 0, 1, -1] # 상하

    def bfs(s, j):
        graph[j][s] = 0
        queue = deque([(s, j)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        queue.append((nx, ny))


    # M: 가로, N: 세로
    m, n, k = list(map(int, input().split()))

    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split()) # X, Y
        graph[y][x] = 1

    count = 0
    for i in range(m): # 가로
        for k in range(n): # 세로
            if graph[k][i] == 1:
                bfs(i, k) # 가로 세로
                count += 1

    print(count)