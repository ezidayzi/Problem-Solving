# 하나의 트리형태
# 전선 하나 끊어서 전력망 네트워크를 2개로 분할
# 송전탑의 개수를 최대한 비슷하게
# 송전탑의 개수 n, 전선 정보 wires -> 전선 들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록
# 두 전력망이 가지고 있는 송전탑 개수의 차이를 return

from collections import deque


def solution(n, wires):
    answer = 10000

    def bfs(v, graph):
        visited[v] = True
        queue = deque([v])
        count = 1

        while queue:
            x = queue.popleft()

            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    count += 1

        return count

    max_wire = 0
    for wire in wires:
        max_wire = max(wire[0], max_wire)
        max_wire = max(wire[1], max_wire)

    ans_array = [[] for i in range(len(wires))]

    for i in range(len(wires)):
        new_wires = wires[:i] + wires[i + 1:]

        graph = [[] for i in range(max_wire + 1)]
        visited = [False] * (max_wire + 1)

        for wire in new_wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])

        for x in range(1, max_wire + 1):
            for node in graph[x]:
                if not visited[node]:
                    ans_array[i].append(bfs(node, graph))

        if len(ans_array[i]) == 1:
            ans_array[i].append(1)

    for ans in ans_array:
        if len(ans) == 2:
            answer = min(answer, abs(ans[0] - ans[1]))

    return answer