from collections import deque

for _ in range(int(input())):
    def bfs(x, y):
        dx = [-2, -1, 1, 2, 2, 1, -1, -2] # 좌우
        dy = [1, 2, 2, 1, -1, -2, -2, -1] # 상하

        queue = deque([(x, y)])

        while len(queue) > 0:
            check = False
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < l and 0 <= ny < l:
                    if graph[ny][nx] == 0:
                        queue.append((nx, ny))
                        graph[ny][nx] = graph[y][x] + 1

        return graph[my][mx]

    l = int(input())
    graph = [[0] * l for _ in range(l)]
    x, y = list(map(int, input().split())) # 나이트가 현재 있는 칸
    mx, my = list(map(int, input().split())) # 나이트가 이동하고자 하는 값
    # 최소 몇번 이동?

    if mx == x and my == y:
        print(0)
    else:
        print(bfs(x, y))