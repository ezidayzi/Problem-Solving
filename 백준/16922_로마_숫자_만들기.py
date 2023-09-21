n = int(input())
number = [1, 5, 10, 50]

ans = []

def dfs(s):
    if len(s) == n:
        if sum(s) not in ans:
            ans.append(sum(s))
        return

    for i in range(4):
        if len(s) == 0:
            s.append(number[i])
            dfs(s)
            s.pop()

        elif number[i] >= max(s):
            s.append(number[i])
            dfs(s)
            s.pop()


dfs([])
print(len(ans))
