import sys
read = sys.stdin.readline

n, c = map(int, read().split(' '))
house = [int(read()) for _ in range(n)]
house.sort()

start = 0
end = max(house)

while start <= end:
    distance = (start + end) // 2
    cnt = 1
    tmp = house[0]
    for i in range(n):
        if house[i] >= distance + tmp:
            tmp = house[i]
            cnt += 1

    if cnt >= c:
        start = distance + 1
    else:
        end = distance - 1
print(end)


