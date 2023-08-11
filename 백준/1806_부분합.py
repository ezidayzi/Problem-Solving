import sys
N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

start = 0
end = 0

m = sys.maxsize
s = 0

while True:
    if s >= S:
        m = min(m, end - start)
        s -= nums[start]
        start += 1
    elif end == N:
        break
    else:
        s += nums[end]
        end += 1

if m == sys.maxsize:
    print(0)
else:
    print(m)