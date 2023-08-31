n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n


def dfs(x, c):
    visited[x] = True
    if c == 4:
        print(1)
        exit(0)

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, c + 1)
            visited[i] = False


for i in range(n):
    dfs(i, 0)
    visited[i] = False

print(0)
