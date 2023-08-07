n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

p1 = 0
p2 = 0

answer = []
while p1 < n and p2 < m:
    x = arr1[p1]
    y = arr2[p2]
    if x < y:
        answer.append(x)
        p1 += 1
    elif x > y:
        answer.append(y)
        p2 += 1
    else:
        answer.append(x)
        answer.append(y)
        p1 += 1
        p2 += 1

if p1 == n:
    for i in range(p2, m):
        answer.append(arr2[i])
elif p2 == m:
    for i in range(p1, n):
        answer.append(arr1[i])

print(" ".join(map(str, answer)))