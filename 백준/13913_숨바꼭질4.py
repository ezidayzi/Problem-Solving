from collections import deque

n, m = map(int, input().split())
visited = [-1] * 200002

queue = deque([(n, 0)])
visited[n] = True

ans = 0
path = []

while queue:
    v, t = queue.popleft()
    if v < 100001 and visited[v * 2] == -1:
        queue.append((v * 2, t + 1))
        visited[v * 2] = v
    if v > 0 and visited[v - 1] == -1:
        queue.append((v - 1, t + 1))
        visited[v - 1] = v
    if v < 200001 and visited[v + 1] == -1:
        queue.append((v + 1, t + 1))
        visited[v + 1] = v
    if v == m:
        ans = t
        idx = v
        while idx != n:
            path.append(idx)
            idx = visited[idx]
        path.append(n)
        break

print(ans)
print(' '.join(map(str, path[::-1])))
