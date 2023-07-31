from collections import deque

n, m = map(int, input().split())
visited = [False] * 200002

queue = deque([(n, 0)])
visited[n] = True

ans = 0

while queue:
    v, t = queue.popleft()
    if v > 0 and not visited[v-1]:
        queue.append((v-1, t+1))
        visited[v-1] = True
    if v < 200001 and not visited[v+1]:
        queue.append((v+1, t+1))
        visited[v + 1] = True
    if v < 100001 and not visited[v*2]:
        queue.append((v*2, t+1))
        visited[v*2] = True
    if v == m:
        ans = t
        break

print(ans)
