def backtracking(idx, cnt):
    global count
    if idx == n:
        if cnt == m:
            count += 1
        return

    for i in range(10):
        if visited[i]:
            visited[i] = False
            backtracking(idx + 1, cnt + 1)
            visited[i] = True
        else:
            backtracking(idx + 1, cnt)


n, m = map(int, input().split())
visited = [False] * 10
count = 0

data = []

if m > 0:
    data = list(map(int, input().split()))

for num in data:
    visited[num] = True

backtracking(0, 0)
print(count)
