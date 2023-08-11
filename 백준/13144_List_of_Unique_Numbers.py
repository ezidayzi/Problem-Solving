N = int(input())
numbers = list(map(int, input().split(' ')))

start = 0
end = 0
seq = [False] * 1000001
cnt = 0

while start < N and end < N:
    if not seq[numbers[end]]:
        seq[numbers[end]] = True
        end += 1
        cnt += (end - start)
    else:
        seq[numbers[start]] = False
        start += 1
print(cnt)