from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
graph = [0] * 100

for _ in range(n + m):
    n1, n2 = map(int, input().split())
    graph[n1 - 1] = n2 - 1

dice = [1, 2, 3, 4, 5, 6]


def bfs():
    q = deque()
    q.append((0, 0))
    graph[0] = -1
    while q:
        x, cnt = q.popleft()

        if x == 99:
            return cnt
        for i in range(6):
            nx = x + dice[i]
            if 0 <= nx < 100 and not graph[nx] == -1:
                if graph[nx] != 0:
                    q.append((graph[nx], cnt + 1))
                else:
                    q.append((nx, cnt + 1))
                graph[nx] = -1


print(bfs())
