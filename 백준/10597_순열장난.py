n = list(map(int, map(str, input())))
N = len(n) if len(n) < 10 else 9 + (len(n) - 9) // 2
visited = [False for _ in range(N + 1)]


def dfs(index, a):
    if index == len(n):
        print(*a)
        exit()

    num = n[index]
    if not visited[num]:
        visited[num] = True
        a.append(num)
        dfs(index + 1, a)
        visited[num] = False
        a.pop()

    if len(n) > index + 1:
        num = n[index] * 10 + n[index + 1]
        if num <= N and not visited[num]:
            visited[num] = True
            a.append(num)
            dfs(index + 2, a)
            visited[num] = False
            a.pop()


dfs(0, [])
