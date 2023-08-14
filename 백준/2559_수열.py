import sys
n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
s = [0] * (n+1)

for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

end = 0
m = -sys.maxsize
while end <= n - k:
    if m <= s[end+k]-s[end]:
        m = max(s[end+k]-s[end], m)
    end += 1

print(m)