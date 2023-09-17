import sys

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
answer = sys.maxsize


def dfs(start, now, cost, cnt):
    global answer

    if cnt == n:
        if graph[now][start]:
            cost += graph[now][start]
            answer = min(answer, cost)
        return

    for i in range(n):
        if not visited[i] and graph[now][i] > 0:
            visited[i] = True
            dfs(start, i, cost+graph[now][i], cnt+1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)
