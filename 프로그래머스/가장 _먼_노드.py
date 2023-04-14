# n개의 노드가 있는 그래프
# 각 노드는 1부터 n까지 번호가 적혀있음
# 1번 노드에서 가장 멀리떨어진 노드의 갯수?
# 가장 멀리 떨어진 노드 = 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드
from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    while queue:
        v = queue.popleft()

        for e in graph[v]:
            if visited[e] == 0:
                queue.append(e)
                visited[e] += visited[v] + 1

    for visit in visited:
        if visit == max(visited):
            answer += 1

    return answer