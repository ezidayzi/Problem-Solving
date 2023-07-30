def dfs(a, b):
    visited[a] = True
    for x in arr[a]:
        if not visited[x]:
            dfs(x, b)
        elif visited[x] and x == b:
            result.append(x)


n = int(input())
arr = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    arr[i].append(int(input()))

result = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)
print(len(result))
result.sort()

for k in result:
    print(k)