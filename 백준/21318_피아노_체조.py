import sys
input = sys.stdin.readline
n = int(input())
numbers = [0] + list(map(int, input().split(' ')))

dp = [0] * (n+1)
for i in range(1, n+1):
    if numbers[i-1] > numbers[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split(' '))
    print(dp[y]-dp[x])