n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

l.reverse()
l.insert(0, [])

dp = [0] * (n+1)

for i in range(1, n+1):
    if i < l[i][0]:
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1], l[i][1] + dp[i-l[i][0]])

print(dp[n])