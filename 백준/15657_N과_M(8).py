n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

a = []
def dfs():
    if len(a) == m:
        print(' '.join(map(str, a)))
        return

    for i in s:
        if len(a) == 0:
            a.append(i)
            dfs()
            a.pop()
        elif i >= a[-1]:
            a.append(i)
            dfs()
            a.pop()

dfs()