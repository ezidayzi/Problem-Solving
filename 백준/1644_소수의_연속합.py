N = int(input())

start = 2
end = 2

check = [True] * (N + 1)
answer = 0
check[0] = False
check[1] = False

m = 0
for i in range(2, N + 1):
    if check[i]:
        m = max(i, m)
        for j in range(i + i, N + 1, i):
            check[j] = False

s = 0
while start < m and end <= m:
    if s == N:
        answer += 1

    if s <= N:
        s += end
        for i in range(end + 1, N + 1):
            if check[i]:
                end = i
                break
    else:
        s -= start
        for i in range(start + 1, N + 1):
            if check[i]:
                start = i
                break

if check[N]:
    answer += 1
print(answer)
