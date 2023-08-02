# RGB 거리
# 집이 N개 있음 거리느 선분ㅇ로 나타낼 수 있음 1번집 부터 N번 집이 순서대로 있음
# 빨 초 파 중 하나의 색으로 칠해야함
# 1번집-2번집 색 달라야함
# N번 집 N-1번집 색 달라야함
# 2~N-1번 집의 색은 양 옆과 색이 달라야함
# 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값

import sys
read = sys.stdin.readline

N = int(read())
cost =[list(map(int, read().split())) for _ in range(N)]


for i in range(1, N):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[-1]))