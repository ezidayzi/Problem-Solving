import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

time = defaultdict(int)
m = 0
for _ in range(n):
    a, b = map(int, input().split())
    time[a] += 1
    time[b] -= 1

ans = 0
cnt = 0
ans_start = 0
ans_end = 0
isUpdated = False
for t in sorted(time.keys()):
    if cnt + time[t] > ans:
        ans_start = t
        ans = cnt + time[t]
        isUpdated = True
    if isUpdated and cnt + time[t] < ans:
        ans_end = t
        isUpdated = False
    cnt += time[t]

print(ans)
print(ans_start, ans_end)
