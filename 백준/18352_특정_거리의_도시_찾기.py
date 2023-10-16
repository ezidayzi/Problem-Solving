from collections import deque

def distance(x):
    queue = deque()
    queue.append((x, 0))

    visited = [False for _ in range(N+1)]
    visited[x] = 1

    ans = []

    while queue:
        v, d = queue.popleft()

        if d == K:
            ans.append(v)

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append((w, d+1))

    return ans


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


ans = distance(X)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    print(*ans, sep='\n')