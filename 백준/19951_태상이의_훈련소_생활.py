import sys

input = sys.stdin.readline

n, m = map(int, input().split())
H = [0] + list(map(int, input().split()))
K = [0] * (n + 2)

for _ in range(m):
    a, b, k = map(int, input().split())
    K[a] += k
    K[b+1] -= k

print(K)
for i in range(n+1):
    K[i+1] += K[i]

for i in range(n+1):
    H[i] += K[i]
print(" ".join(map(str, H[1:])))