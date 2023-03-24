from collections import deque


def dfs(s):
    visited[s] = True
    print(s, end=' ')
    for i in graph[s]:
        if not visited[i]:
            dfs(i)


def bfs(s):
    queue = deque([s])
    visited[s] = True
    print(s, end=' ')

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')



arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]
v = arr[2]

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, p = map(int, input().split())
    graph[u].append(p)
    graph[p].append(u)

for i in range(n+1):
    graph[i].sort()

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
