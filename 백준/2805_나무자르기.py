n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for t in arr:
        if t > mid:
            total += t - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)