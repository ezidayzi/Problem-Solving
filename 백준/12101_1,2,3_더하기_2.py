n, k = map(int, input().split())
ans = []


def backtracking(x):
    if sum(x) == n:
        ans.append(x[:])
        return
    elif sum(x) >= n:
        return
    else:
        x.append(1)
        backtracking(x)
        x.pop()

        x.append(2)
        backtracking(x)
        x.pop()

        x.append(3)
        backtracking(x)
        x.pop()


backtracking([])

if k <= len(ans):
    print('+'.join(map(str, ans[k-1])))
else:
    print(-1)
