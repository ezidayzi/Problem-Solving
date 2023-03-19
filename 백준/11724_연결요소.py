import sys
sys.setrecursionlimit(10000) # 재귀 제한 -> 작성해줘야 런타임 에러가 안남

def dfs(graph, v, visited):
    visited[v] = True # 방문

    # 연결되어 있는 곳 전부 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



n, m = map(int, sys.stdin.readline().split())

# 그래프 노드는 1부터 시작임
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        ans += 1

print(ans)
