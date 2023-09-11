n, m = map(int, input().split())

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if len(s) == 0:
            s.append(i)
            dfs()
            s.pop()
        elif i not in s and i > s[-1]:
            s.append(i)
            dfs()
            s.pop()

dfs()