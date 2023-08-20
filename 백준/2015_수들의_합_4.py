import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))

p_sum = {0: 1}
current_sum = 0

ans = 0
for num in A:
    current_sum += num
    if current_sum - k in p_sum:
        ans += p_sum[current_sum-k]

    if current_sum in p_sum:
        p_sum[current_sum] += 1
    else:
        p_sum[current_sum] = 1

print(ans)