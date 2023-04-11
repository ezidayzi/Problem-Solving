# 캐릭터는 동서 납북 방향으로 한칸씩 이동
# 0은 벽이 있는 자리, 1은 벽이 없는 자리

# 최단 경로는 bfs
from collections import deque


def solution(maps):
    answer = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps)  # 세로 y
    m = len(maps[0])  # 가로 x

    def bfs(x, y):
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        queue.append((nx, ny))

        print(maps)
        return maps[n - 1][m - 1]

    answer = bfs(0, 0)
    if answer == 1:
        answer = -1

    return answer