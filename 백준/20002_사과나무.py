import sys

input = sys.stdin.readline
n = int(input())
A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

DP = [[0 for i in range(0, n + 1)] for _ in range(n + 1)]

ans = -sys.maxsize
for x in range(1, n + 1):
    for y in range(1, n + 1):
        DP[x][y] = DP[x][y - 1] + DP[x - 1][y] - DP[x - 1][y - 1] + A[x - 1][y - 1]
        for i in range(x):
            for j in range(y):
                if x - i != y - j: continue
                current_sum = DP[x][y] - DP[x][j] - DP[i][y] + DP[i][j]
                ans = max(ans, current_sum)

print(ans)
