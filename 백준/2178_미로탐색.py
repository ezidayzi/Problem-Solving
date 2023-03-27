from collections import deque

def bfs(x, y):
    count = 0
    dx = [1, -1, 0, 0] # 좌우
    dy = [0, 0, 1, -1] # 상하

    queue = deque([(x, y)])
    arr[y][x] = 0

    while len(queue) > 0:
        check = False
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == 1:
                    queue.append((nx, ny))
                    arr[ny][nx] = 0
                    dp[ny][nx] = dp[y][x] + 1

    return dp[n-1][m-1]


n, m = list(map(int, input().split()))
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

print(bfs(0, 0))