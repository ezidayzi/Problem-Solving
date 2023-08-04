import sys
read = sys.stdin.readline

N = int(read())
dp = [0 for i in range(N+1)]

ans = []
for i in range(2, N+1):
    a = []
    if i - 1 > 0:
        a.append(dp[i-1])
    if i % 2 == 0:
        a.append(dp[i//2])
    if i % 3 == 0:
        a.append(dp[i//3])

    dp[i] = min(a)+1

print(dp[N])

res = [N]
now = N
temp = dp[N] - 1

# n부터 하나씩 줄여나가면서 순서 찾기
for i in range(N, 0, -1):
    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        res.append(i)
        temp -= 1

print(*res)