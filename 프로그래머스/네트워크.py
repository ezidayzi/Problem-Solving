def solution(n, computers):
    answer = 0

    visited = []

    def dfs(i):
        for j in range(n):
            if j not in visited and computers[i][j] == 1:
                visited.append(j)
                dfs(j)

    for i in range(n):
        if i not in visited:
            visited.append(i)
            dfs(i)
            answer = answer + 1

    return answer