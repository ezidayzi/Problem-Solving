from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(x):
    visited = [False] * (n + 1)
    q = deque([x])
    cnt = 0
    visited[x] = True
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True

    return cnt


ans = []
maxCnt = 0
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)
