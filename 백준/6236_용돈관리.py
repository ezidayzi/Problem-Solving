# K원만 인출
# 하루를 보낼 수 있으면 그대로 사용, 모자라면 남은 금액은 다시 통장, 다시 K원 인출
# M번을 맞추기 위해 남은 금액 > 사용할 금액 -> 남은 금액은 통장에 넣고 다시 K원 인출
# 최소 금액 K

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

left = min(arr) # 최소 금액
right = sum(arr) # 최대 금액

while left <= right:
    mid = (left + right) // 2 # 목표값
    charge = mid
    num = 1
    for i in range(n):
        if charge < arr[i]:
            charge = mid
            num += 1
        charge -= arr[i]

    if num > m or mid < max(arr): # 출금 횟수가 M보다 크면 left 증가
        left = mid + 1
    else: # M보다 작거나 같으면 right 감
        right = mid - 1
        k = mid
print(k)