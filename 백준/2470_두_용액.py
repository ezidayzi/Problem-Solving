import sys
read = sys.stdin.readline

n = int(read())
liquid = list(map(int, read().split(' ')))
liquid.sort()

start = 0
end = n - 1

s = 1000000001 * 2
a, b = 1000000001, 1000000001

while start < end:
    c = liquid[start] + liquid[end]
    if abs(c) < s:
        s = abs(c)
        a = liquid[start]
        b = liquid[end]

    if liquid[start] + liquid[end] < 0:
        start = start + 1
    else:
        end = end - 1

print(a, b)
