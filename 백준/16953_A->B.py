a, b = map(int, input().split())

def dfs(x, d):
    global ans
    if x == b:
        print(d)
        exit(0)
    if x > b:
        return

    dfs(10*x+1, d+1)
    dfs(x * 2, d+1)

dfs(a, 1)

print(-1)
