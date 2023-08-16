import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

DP = [[0 for i in range(0, n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        DP[i][j] = DP[i][j - 1] + DP[i - 1][j] - DP[i - 1][j - 1] + A[i - 1][j - 1]

for _ in range(m):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j - 1] - DP[i - 1][y] + DP[i - 1][j - 1])
