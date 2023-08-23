import sys

input = sys.stdin.readline
r, c, q = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(r)]

DP = [[0 for i in range(0, c + 1)] for _ in range(r + 1)]

for i in range(1, r + 1):
    for j in range(1, c + 1):
        DP[i][j] = DP[i][j - 1] + DP[i - 1][j] - DP[i - 1][j - 1] + f[i - 1][j - 1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    v = DP[r2][c2] - DP[r2][c1 - 1] - DP[r1 - 1][c2] + DP[r1 - 1][c1 - 1]
    s = ((r2 - r1 + 1) * (c2 - c1 + 1))
    print(v // s)
