n = int(input())
money = list(map(int, input().split()))
M = int(input())

start = 0
end = max(money)

result = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for m in money:
        if m < mid:
            sum += m
        else:
            sum += mid
    if sum <= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)