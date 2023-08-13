import sys
N, M = map(int, input().split(' '))
A = [int(input()) for i in range(N)]

A.sort()

start = 0
end = 0

ans = sys.maxsize
while start < N and end < N:
    if A[end] - A[start] >= M:
        ans = min(ans, A[end]-A[start])
        start += 1
    else:
        end += 1

if sys.maxsize == ans:
    print(0)
else:
    print(ans)