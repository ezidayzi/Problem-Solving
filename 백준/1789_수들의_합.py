n = int(input())

s = 1
e = n

ans = 0
while s <= e:
    mid = (s + e) // 2
    if mid * (mid + 1) / 2 <= n:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)