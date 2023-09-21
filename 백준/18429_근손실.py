n, k = map(int, input().split())
l = list(map(int, input().split()))

ans = 0


def dfs(w, r):
    global ans

    if len(r) == n:
        ans += 1
        return

    for i in range(n):
        if w + l[i] - k >= 500 and i not in r:
            r.append(i)
            dfs(w + l[i] - k, r)
            r.pop()


dfs(500, [])
print(ans)