n = int(input())
skill = [list(map(int, input().split())) for _ in range(n)]
start = []

ans = 1e9
def backtracking():
    global start
    global ans
    if len(start) == n/2:
        link = [i for i in range(n) if i not in start]

        start_skill = 0
        for x in start:
            for y in start:
                start_skill += skill[x][y]

        link_skill = 0
        for x in link:
            for y in link:
                link_skill += skill[x][y]

        ans = min(ans, abs(start_skill-link_skill))
        return

    for i in range(0, n):
        if len(start) == 0:
            start.append(i)
            backtracking()
            start.pop()
        elif i not in start and i > start[-1]:
            start.append(i)
            backtracking()
            start.pop()


backtracking()
print(ans)