from collections import deque

n, m = map(int, input().split())
MAX_SIZE = 100001
visited = [-1] * MAX_SIZE
visited[n] = 0
queue = deque([n])
cnt = 0

while queue:
    v = queue.popleft()

    if v == m:
        cnt += 1

    for next in [v * 2, v + 1, v - 1]:
        if 0 <= next < MAX_SIZE:
            if visited[next] == -1 or visited[next] == visited[v] + 1:
                visited[next] = visited[v] + 1
                queue.append(next)


print(visited[m])
print(cnt)
