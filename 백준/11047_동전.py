import sys

n, k = list(map(int, sys.stdin.readline().split()))

money = []
for _ in range(n):
    money.append(int(sys.stdin.readline()))

count = 0
i = n - 1

while True:
    if i < 0:
        break
    if k == 0:
        break
    if k >= money[i]:
        c, d = divmod(k, money[i])
        k = d
        count += c
    else:
        i = i-1


print(count)
