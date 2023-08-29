N = int(input())

arr = list(map(int, input().split()))

erase = int(input())


def dfs(index):
    arr[index] = -2
    for i in range(N):
        if arr[i] == index:
            dfs(i)


dfs(erase)
answer = 0

# 리프인지 확인하는 방법
for i in range(N):
    if not arr[i] == -2 and i not in arr:
        answer += 1

print(answer)
