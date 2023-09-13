n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
visited = [False] * n

a = []
def dfs():
    if len(a) == m:
        print(' '.join(map(str, a)))
        return

    overlap = 0
    for i in range(len(s)):
        if overlap != s[i]:
            visited[i] = True
            a.append(s[i])
            overlap = s[i]
            dfs()
            a.pop()
            visited[i] = False

dfs()