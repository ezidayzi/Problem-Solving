import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))
l.sort()

for i in range(1, n+1):
    l[i] += l[i-1]

for _ in range(m):
    x, y = map(int, input().split())
    print(l[y]-l[x-1])