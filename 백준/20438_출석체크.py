import sys
input = sys.stdin.readline
n, k, q, m = map(int, input().split())
sleep = list(map(int, input().split())) # k명의 졸고있는 학생
code = list(map(int, input().split())) # q개의 입장코드

check = [0] * (n+3)

for c in code:
    if c in sleep:
        continue
    for i in range(c, n+3, c):
        if i not in sleep:
            check[i] = 1

pre_sum = [0] * (n+3)

for i in range(3, n+3):
    if check[i] == 0:
        pre_sum[i] = pre_sum[i-1] + 1
    else:
        pre_sum[i] = pre_sum[i - 1]

for i in range(m):
    s, e = map(int, input().split())
    print(pre_sum[e]-pre_sum[s-1])
