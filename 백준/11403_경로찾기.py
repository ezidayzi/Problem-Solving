N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 플로이드-워셜 알고리즘
for k in range(N):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            # 바로 방문할 수 있거나, 연결되어 있어서 방문할 수 있는 경우 1로 교체
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

# 출력
for row in graph:
    for col in row:
        print(col, end=" ")
    print()
