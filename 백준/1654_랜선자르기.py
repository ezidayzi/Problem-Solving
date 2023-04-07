k, n = list(map(int, input().split()))
lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)
ans = [0]

while start <= end:
    mid = (start + end) // 2

    count = 0
    for line in lines:
        count += line // mid

    if count < n:
        end = mid - 1
    else: # n개보다 많이 만드는 것도 포함
        ans.append(mid)
        start = mid + 1

print(max(ans))