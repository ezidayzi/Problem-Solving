def solution(tickets):
    answer = []

    visited = [False] * len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])
    print(answer)
    answer.sort()

    # 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    return answer[0]