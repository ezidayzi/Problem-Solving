from collections import deque

# BFS
def bfs(graph, node, visited):
    cnt = 0
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                check[i] = check[v] + 1


n = int(input())
x, y = list(map(int, input().split()))

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
bfs(graph, x, visited)

print(check[y] if check[y] > 0 else -1)

# DFS

def dfs(s):
    for i in graph[s]:
        if check[i] == 0:
            check[i] = check[s] + 1
            dfs(i)


n = int(input())
x, y = list(map(int, input().split()))

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(x)
print(check[y] if check[y] > 0 else -1)