n = int(input())
mp, mf, ms, mv = map(int, input().split())  # 최소 영양분
ing = []
for _ in range(n):
    ing.append(list(map(int, input().split())))

ans = 1e9
l = []

ans_l = []
def backtracking(p, f, s, v, cost):
    global ans
    global ans_l
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if ans > cost:
            ans = cost
            ans_l = l[:]
        return

    for i in range(n):
        if not l:
            l.append(i)
            backtracking(p + ing[i][0], f + ing[i][1], s + ing[i][2], v + ing[i][3], cost + ing[i][4])
            l.pop()
        elif l[-1] < i and i not in l:
            l.append(i)
            backtracking(p + ing[i][0], f + ing[i][1], s + ing[i][2], v + ing[i][3], cost + ing[i][4])
            l.pop()


backtracking(0, 0, 0, 0, 0)
if ans_l:
    print(ans)
    for i in ans_l:
        print(i+1, end=' ')
else:
    print(-1)
