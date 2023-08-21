import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))

r = [0] * m
psum = 0

for i in range(n):
    psum += num[i]
    r[psum % m] += 1

cnt = r[0]

for i in r:
    cnt += i * (i - 1) // 2

print(cnt)