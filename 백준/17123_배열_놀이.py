import sys

input = sys.stdin.readline

t = int(input())  # test case

for _ in range(t):
    n, m = map(int, input().split())  # 행, 열

    A = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    rsum = [0] * (n + 1)
    csum = [0] * (n + 1)

    for r in range(n + 1):
        for c in range(n + 1):
            rsum[r] += A[r][c]

    for c in range(n + 1):
        for r in range(n + 1):
            csum[c] += A[r][c]

    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for r in range(c1, c2 + 1):
            csum[r] += v * (r2 - r1 + 1)
        for c in range(r1, r2 + 1):
            rsum[c] += v * (c2 - c1 + 1)

    print(' '.join(map(str, rsum[1:])))
    print(' '.join(map(str, csum[1:])))
