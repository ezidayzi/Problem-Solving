n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

a = []
def dfs():
    if len(a) == m:
        print(' '.join(map(str, a)))
        return

    for i in s:
        if i not in a:
            a.append(i)
            dfs()
            a.pop()

dfs()