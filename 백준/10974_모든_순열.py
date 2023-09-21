n = int(input())

def dfs(a):
    if len(a) == n:
        print(*a)
        return

    for i in range(1, n+1):
        if not i in a:
            a.append(i)
            dfs(a)
            a.pop()

dfs([])